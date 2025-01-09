🏦 Banking System Application 💳
Welcome to the Banking System Application! 🚀
This is a simple Python-based banking system that allows users to manage their accounts, 
perform transactions, and ensure secure financial operations. 🌐🔒

💡 Features
User Registration 📝

Register new users with details like name, contact, email, and address.
Set an initial balance upon account creation. 💰
Passwords are securely hashed with bcrypt. 🔐
Login System 🔑

Login using your account number and password.
Secure password validation with bcrypt. ✅
Account Management 💼

Check your balance anytime. 📊
Credit funds to your account. 💵
Debit funds from your account (ensuring a minimum balance of ₹2000). 💳
Security 🔒

Passwords are hashed and checked securely. 🔑
Balance operations ensure no account goes below the minimum balance.
🛠️ Technologies Used
Python 🐍
MySQL 💾
bcrypt 🔐 (for password hashing)
🚀 How to Run
Clone this repository:

bash
Copy code
https://github.com/Vicky9010/banking-system.git
Install the required libraries:

bash
Copy code
pip install mysql-connector-python bcrypt
Set up your MySQL database with the schema for users and login.
Example schema:

sql
Copy code
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    account_number VARCHAR(255) UNIQUE,
    contact_number VARCHAR(20),
    email VARCHAR(255),
    address TEXT,
    dob DATE,
    city VARCHAR(100),
    balance DECIMAL(15, 2)
);

CREATE TABLE login (
    user_id INT,
    password VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES users(id)
);
Run the Python program:

bash
Copy code
python banking_system.py
📚 Features Walkthrough
Register a User 🧑‍💻
You can register a new user by providing personal details and an initial balance.

Login 🏷️
Enter your account number and password to access your account.

Show Balance 💵
Check the current balance in your account.

Credit Amount 💸
Add funds to your account.

Debit Amount 💳
Withdraw funds while ensuring the balance doesn’t go below ₹2000.

Logout 🚪
Securely log out of your account.

🤖 Contributing
Fork this repository 🍴
Clone your forked repository 💻
Create a new branch 🧑‍💻
Make your changes 🛠️
Commit your changes and push 🚀
Open a pull request 🔄

Thank you for checking out this project! 🙏
Happy coding and stay secure! 😄

