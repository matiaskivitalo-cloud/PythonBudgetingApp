"""SQLite database implementation for the budgeting application."""

import sqlite3

from models import Transaction

CREATE_TRANSACTIONS_TABLE = """CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL NOT NULL,
    type TEXT NOT NULL,
    date TEXT NOT NULL,
    description TEXT,
    category TEXT
)"""

def initialize_database():
    """Initialize the database and create necessary tables."""
    connection = sqlite3.connect("budgeting_app.db")
    cursor = connection.cursor()
    cursor.execute(CREATE_TRANSACTIONS_TABLE)
    connection.commit()
    connection.close()

def add_transaction(transaction):
    """Add a transaction to the database."""
    connection = sqlite3.connect("budgeting_app.db")
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO transactions (amount, type, date, description, category) VALUES (?, ?, ?, ?, ?)",
        (transaction.amount, transaction.type, transaction.date, transaction.description, transaction.category)
    )
    connection.commit()
    connection.close()

def get_all_transactions():
    """Retrieve all transactions from the database."""

    connection = sqlite3.connect("budgeting_app.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM transactions")
    transactions = cursor.fetchall()
    connection.close()

    transaction_objects_dict = {}
    for transaction in transactions:
        transaction_obj = Transaction(
            amount=transaction[1],
            date=transaction[3],
            description=transaction[4],
            id=transaction[0],
            category=transaction[5]
        )
        transaction_objects_dict[transaction[0]] = transaction_obj
    return transaction_objects_dict
