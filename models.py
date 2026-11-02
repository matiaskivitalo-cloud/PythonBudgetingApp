"""File containing the models for the application."""

class Transaction:
    """Class representing a financial transaction."""

    def __init__(self, amount, date, description):
        self.amount = amount
        self.type = "income" if amount >= 0 else "expense"
        self.date = date
        self.description = description
        self.category = None  # Optional category for the transaction


    def __str__(self):
        return f"Transaction(type={self.type}, amount={self.amount}, date={self.date}, description='{self.description}', category={self.category})"

    def set_category(self, category):
        """Set the category for the transaction."""
        self.category = category

    def get_category(self):
        """Get the category of the transaction."""
        return self.category

    def get_type(self):
        """Get the type of the transaction (income or expense)."""
        return self.type

    def get_amount(self):
        """Get the amount of the transaction."""
        return self.amount

    def set_amount(self, amount):
        """Set the amount of the transaction."""
        self.amount = amount
        self.type = "income" if amount >= 0 else "expense"

    def get_date(self):
        """Get the date of the transaction."""
        return self.date

    def get_description(self):
        """Get the description of the transaction."""
        return self.description

    def set_description(self, description):
        """Set the description of the transaction."""
        self.description = description