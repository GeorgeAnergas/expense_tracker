# Expense Tracker

A Python application for tracking personal income and expenses.

Users can add income and expenses, view their transactions, check their balance, and search transactions by category.

All transactions are saved in a local JSON file.


## Features

- Add income and expense transactions
- View all transactions
- Calculate total income and expenses
- Check the current balance
- Search transactions by category
- Save and load transactions using JSON
- Validate transaction types and amounts


## Technologies Used

- Python 3
- JSON
- Python standard library (json, datetime)


## Project Structure

expense_tracker/
│
|-- data/
|   -- transactions.json
|
|-- main.py
|-- transaction.py
|-- expense_manager.py
|-- storage.py
|-- README.md


## Installation and Usage

Clone the repository:

git clone https://github.com/GeorgeAnergas/expense_tracker.git

Navigate to the project folder:

cd expense-tracker

Run the application:

python main.py


## How to Use

Select an option from the main menu:
- Add income: Record a new income transaction.
- Add expense: Record a new expense transaction.
- View transactions: Display all saved transactions.
- View balance: Display total income, total expenses, and current balance.
- Search by category: Find transactions belonging to a specific category.
- Exit: Close the application.


## Data Storage

Transactions are stored locally in data/transactions.json.

When the application starts, previously saved transactions are loaded from the file. New transactions are saved automatically.