import json
from transaction import Transaction

class Storage:
    def __init__(self, file_path):
        self.file_path = file_path

# Save transactions to a JSON file
    def save_transactions(self, transactions):
        data = []
        for transaction in transactions:
            transaction_data = {
                "id": transaction.id,
                "transaction_type": transaction.transaction_type,
                "amount": transaction.amount,
                "category": transaction.category,
                "description": transaction.description,
                "date": transaction.date
            }
            data.append(transaction_data)
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

# Load transactions from a JSON file
    def load_transactions(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("Invalid JSON file.")
            return []
        transactions = []
        for transaction_data in data:
            transaction = Transaction(
                transaction_data["id"],
                transaction_data["transaction_type"],
                transaction_data["amount"],
                transaction_data["category"],
                transaction_data["description"],
                transaction_data["date"]
            )
            transactions.append(transaction)
        return transactions