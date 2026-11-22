# Represents a single financial transaction
class Transaction:
    def __init__(self, transaction_id, transaction_type, amount, category, description, date):
        self.id = transaction_id
        self.transaction_type = transaction_type
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date
        self.validate()
        
# Validate transaction data
    def validate(self):
        if self.transaction_type != "income" and self.transaction_type != "expense":
            raise ValueError("Transaction must be income or expense")
        if self.amount <= 0:
            raise ValueError("Amount must be positive number")

    def __str__(self):
        return (
            f"ID: {self.id} | "
            f"Type: {self.transaction_type} | "
            f"Amount: {self.amount} | "
            f"Category: {self.category} | "
            f"Description: {self.description} | "
            f"Date: {self.date}"
        )