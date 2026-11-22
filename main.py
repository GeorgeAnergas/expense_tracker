from expense_manager import ExpenseManager
from storage import Storage
from transaction import Transaction
from datetime import date

# Initialize manager and storage
manager = ExpenseManager()
storage = Storage("data/transactions.json")

# Load previously saved transactions
manager.transactions = storage.load_transactions()

def show_menu():
    print("\n1. Add income")
    print("2. Add expense")
    print("3. View transactions")
    print("4. View balance")
    print("5. Search by category")
    print("6. Exit")

def create_transaction(transaction_type, manager, storage):
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Amount must be positive.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
        
    category = input("Enter category: ")
    description = input("Enter description: ")
    transaction_date = date.today().isoformat()
    transaction_id = len(manager.transactions) + 1
    transaction = Transaction(
        transaction_id,
        transaction_type,
        amount,
        category,
        description,
        transaction_date
    )
    manager.add_transaction(transaction)
    storage.save_transactions(manager.get_transactions())
    print("Transaction added successfully!")

def view_transactions(manager):
    transactions = manager.get_transactions()
    if not transactions:
        print("No transactions found.")
        return
    for transaction in transactions:
        print(transaction)

def view_balance(manager):
    income = manager.calculate_income()
    expenses = manager.calculate_expenses()
    balance = manager.calculate_balance()
    print(f"Total income: {income}")
    print(f"Total expenses: {expenses}")
    print(f"Balance: {balance}")

def search_by_category(manager):
    category = input("Enter category: ")
    results = manager.search_transaction(category)
    if not results:
        print("No transactions found.")
        return
    for transaction in results:
        print(transaction)

# Main application loop
while True:
    show_menu()
    choice = input("Choose an option: ")
    match choice:
        case "1":
            create_transaction("income", manager, storage)
        case "2":
            create_transaction("expense", manager, storage)
        case "3":
            view_transactions(manager)
        case "4":
            view_balance(manager)
        case "5":
            search_by_category(manager)
        case "6":
            print("Goodbye")
            break
        case _:
            print("Invalid choice. Please try again!")

