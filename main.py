""" This is a simple budgeting app that allows users to track their income and expenses.
Users can add income and expense entries, view their current balance, and generate reports to analyze their
 spending habits. The app provides a user-friendly interface and supports multiple categories for better organization of financial data.
Features:
- Add income and expense entries with details such as amount, category, and date.
"""

import database

from models import Transaction

def main():
    """Main function to run the budgeting app."""
    database.initialize_database()

    while True:
        print("\nBudgeting App Menu:")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            amount = float(input("Enter the amount: "))
            date = input("Enter the date (YYYY-MM-DD): ")
            description = input("Enter a description: ")
            category = input("Enter a category (optional): ")

            transaction = Transaction(amount=amount, date=date, description=description, category=category)
            database.add_transaction(transaction)
            print("Transaction added successfully!")

        elif choice == "2":
            transactions = database.get_all_transactions()
            if not transactions:
                print("No transactions found.")
            else:
                for transaction_id, transaction in transactions.items():
                    print(transaction)

        elif choice == "3":
            print("Exiting the app. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()