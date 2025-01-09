import mysql.connector
import random
import bcrypt
from decimal import Decimal

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",  # Your MySQL username
    password="Thakur99@",  # Your MySQL password
    database="banking_system"
)
cursor = db.cursor()

def display_welcome_message():
    print("******************************************")
    print("*           Welcome to the Banking      *")
    print("*          System Application          *")
    print("*       Manage your account with ease  *")
    print("*        and secure your finances!     *")
    print("******************************************")
    print("\n")

# Helper function to generate a unique account number
def generate_account_number():
    return str(random.randint(1000000000, 9999999999))

# Hash password using bcrypt (ensure password is encoded as bytes)                                      
def hash_password(password):
    if isinstance(password, str):
        password = password.encode('utf-8')  # Convert password string to bytes
    return bcrypt.hashpw(password, bcrypt.gensalt())

# Check password (ensure the stored hash and the password are both in bytes)
def check_password(stored_hash, password):
    # Convert the stored hash (if it is a string) to bytes
    if isinstance(stored_hash, str):
        stored_hash = stored_hash.encode('utf-8')  # Ensure stored hash is in bytes

    if isinstance(password, str):
        password = password.encode('utf-8')  # Convert password string to bytes

    return bcrypt.checkpw(password, stored_hash)

# User registration function
def add_user(name, contact, email, address, dob, city, initial_balance, password):
    account_number = generate_account_number()
    
    # Hash the password
    hashed_password = hash_password(password)

    # Insert user into the database
    try:
        cursor.execute("INSERT INTO users (name, account_number, contact_number, email, address, dob, city, balance) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                       (name, account_number, contact, email, address, dob, city, initial_balance))
        db.commit()
        user_id = cursor.lastrowid  # Get the inserted user's ID

        cursor.execute("INSERT INTO login (user_id, password) VALUES (%s, %s)", (user_id, hashed_password))
        db.commit()
        print(f"User {name} added successfully with account number {account_number}.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Login function
def login(account_number, password):
    """Login function that checks account number and password."""
    cursor.execute("SELECT u.id, l.password FROM users u JOIN login l ON u.id = l.user_id WHERE u.account_number = %s", (account_number,))
    user = cursor.fetchone()

    if user:
        # Account number exists, now check if the password matches
        if check_password(user[1], password):
            print("Login successful!")
            return user[0]  # Return user ID on successful login
        else:
            print("Incorrect password. Please try again.")
            return None
    else:
        # Account number doesn't exist
        print("Invalid account number.")
        return None

# Show balance function
def show_balance(user_id):
    cursor.execute("SELECT balance FROM users WHERE id = %s", (user_id,))
    balance = cursor.fetchone()
    if balance:
        print(f"Current balance: {balance[0]}")

# Credit amount function
def credit_amount(user_id, amount):
    cursor.execute("UPDATE users SET balance = balance + %s WHERE id = %s", (amount, user_id))
    db.commit()
    print(f"Amount credited: {amount}")

# Debit amount function
def debit_amount(user_id, amount):
    cursor.execute("SELECT balance FROM users WHERE id = %s", (user_id,))
    balance = cursor.fetchone()[0]

    # Convert balance to Decimal if its not already Decimal (just to be safe)
    if not isinstance(balance, Decimal):
        balance = Decimal(balance)

    # Convert amount to Decimal to match the type of balance
    amount = Decimal(amount)

    if balance >= amount:
        if balance - amount >= 2000:  # Ensuring the balance doesn't go below 2000
            cursor.execute("UPDATE users SET balance = balance - %s WHERE id = %s", (amount, user_id))
            db.commit()
            print(f"Amount debited: {amount}")
        else:
            print("Insufficient balance. You cannot debit below 2000.")
    else:
        print("Insufficient balance.")

# Main program
def main():
    display_welcome_message()

    while True:
        print("\n1. Add User")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            contact = input("Enter contact number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            dob = input("Enter date of birth (YYYY-MM-DD): ")
            city = input("Enter city: ")
            initial_balance = float(input("Enter initial balance: "))
            password = input("Enter password: ")

            add_user(name, contact, email, address, dob, city, initial_balance, password)

        elif choice == "2":
            account_number = input("Enter account number: ")
            password = input("Enter password: ")
            user_id = login(account_number, password)
            if user_id:
                while True:
                    print("\n1. Show Balance")
                    print("2. Credit Amount")
                    print("3. Debit Amount")
                    print("4. Logout")
                    
                    user_choice = input("Enter your choice: ")

                    if user_choice == "1":
                        show_balance(user_id)
                    elif user_choice == "2":
                        amount = float(input("Enter amount to credit: "))
                        credit_amount(user_id, amount)
                    elif user_choice == "3":
                        amount = float(input("Enter amount to debit: "))
                        debit_amount(user_id, amount)
                    elif user_choice == "4":
                        print("Logged out successfully.")
                        break
                    else:
                        print("Invalid choice.")
            else:
                print("Login failed. Please try again.") 

        elif choice == "3":
            print("Exiting system...")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
