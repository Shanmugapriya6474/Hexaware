import sqlite3
from sqlite3 import Connection


class DBUtil:

    @staticmethod
    def getDBConn() -> Connection:
        """
        Establish a connection to the database and return the connection reference.
        """
        try:
            conn = sqlite3.connect('bank_database.db')
            return conn
        except sqlite3.Error as e:
            print(f"Error while connecting to database: {e}")
            raise

    @staticmethod
    def initialize_database():
        """
        Create required tables if they don't exist.
        """
        try:
            conn = DBUtil.getDBConn()
            cursor = conn.cursor()

            # Create customers table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS customers (
                    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    phone TEXT NOT NULL
                )
            """)

            # Create accounts table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS accounts (
                    account_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer_id INTEGER,
                    acc_no INTEGER UNIQUE,
                    acc_type TEXT,
                    balance REAL,
                    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
                )
            """)

            # Optional: Create transactions table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS transactions (
                    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    account_number INTEGER,
                    type TEXT,
                    amount REAL,
                    date TEXT,
                    FOREIGN KEY (account_number) REFERENCES accounts(acc_no)
                )
            """)

            conn.commit()
            cursor.close()
            conn.close()
            print("Database initialized successfully.")
        except sqlite3.Error as e:
            print(f"Database initialization error: {e}")
            raise

