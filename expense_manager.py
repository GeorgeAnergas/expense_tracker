from transaction import Transaction

class ExpenseManager:
    def __init__(self):
        self.transactions = []

# Add a new transaction
    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_transactions(self):
        return self.transactions

# Search transactions by category
    def search_transaction(self, category):
        results = []
        for transaction in self.transactions:
            if transaction.category == category:
                results.append(transaction)
        return results

# Calculate total income
    def calculate_income(self):
        total = 0
        for transaction in self.transactions:
            if transaction.transaction_type == "income":
                total += transaction.amount
        return total

# Calculate total expenses
    def calculate_expenses(self):
        total = 0
        for transaction in self.transactions:
            if transaction.transaction_type == "expense":
                total += transaction.amount
        return total

# Calculate remaining balance
    def calculate_balance(self):
        balance = self.calculate_income() - self.calculate_expenses()
        return balance