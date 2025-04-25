import sqlite3
from repository.i_bank_repository import IBankRepository
from entity.customer import Customer
from entity.account import Account
from entity.transaction import Transaction
from datetime import date
from typing import List
from repository.db_util import DBUtil
from entity.savings_account import SavingsAccount
from entity.current_account import CurrentAccount
from dao.account_dao import AccountDAO

class BankRepositoryImpl(IBankRepository):

    def __init__(self):
        self.accountList = []
        self.accountList.append(Account)

    def __init__(self):
        self.account_dao = AccountDAO()
        self.accountList = []

    def create_account(self, customer, acc_no, acc_type, balance):
        # Check if account number already exists
        conn = DBUtil.getDBConn()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM accounts WHERE acc_no = ?", (acc_no,))
        existing_accounts = cursor.fetchone()
        cursor.close()
        conn.close()

        if existing_accounts[0] > 0:
            raise ValueError(f"Account number {acc_no} already exists. Please use a unique account number.")

        # Proceed to create account if no existing account number found
        if acc_type.lower() == "savings":
            if balance < 500:
                raise ValueError("Minimum balance for savings account is 500")
            account = SavingsAccount(customer, balance, 3.5)
        elif acc_type.lower() == "current":
            account = CurrentAccount(customer, balance, 2000)
        elif acc_type.lower() == "zerobalance":
            account = ZeroBalanceAccount(customer, balance)
        else:
            raise ValueError("Invalid account type")

        account.account_number = acc_no  # overriding auto-generation
        self.accountList.append(account)
        self.account_dao.add_account(account)
        return account

    def list_accounts(self) -> List[Account]:
        conn = DBUtil.getDBConn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM accounts")
        rows = cursor.fetchall()
        accounts = []
        for row in rows:
            # Assuming columns: id, acc_no, acc_type, balance, customer_id
            customer = self.get_customer_by_id(row[4])  # Fetching customer by id (assuming it's the last column)
            accounts.append(Account(row[1], row[2], row[3], customer))
        cursor.close()
        conn.close()
        return accounts

    def calculate_interest(self) -> None:
        # Assuming the calculation of interest is only for savings accounts
        conn = DBUtil.getDBConn()
        cursor = conn.cursor()
        cursor.execute("SELECT acc_no, balance, interest_rate FROM accounts WHERE acc_type='Savings'")
        rows = cursor.fetchall()
        for row in rows:
            new_balance = row[1] * (1 + (row[2] / 100))  # Simple interest calculation
            cursor.execute("UPDATE accounts SET balance=? WHERE acc_no=?", (new_balance, row[0]))
        conn.commit()
        cursor.close()
        conn.close()

    def get_account_balance(self, account_number: int) -> float:
        conn = DBUtil.getDBConn()
        cursor = conn.cursor()
        cursor.execute("SELECT balance FROM accounts WHERE acc_no=?", (account_number,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return row[0] if row else 0.0

    def deposit(self, account_number: int, amount: float) -> float:
        conn = DBUtil.getDBConn()
        cursor = conn.cursor()
        cursor.execute("UPDATE accounts SET balance=balance + ? WHERE acc_no=?", (amount, account_number))
        conn.commit()
        new_balance = self.get_account_balance(account_number)
        cursor.close()
        conn.close()
        return new_balance

    def withdraw(self, account_number: int, amount: float) -> float:
        conn = DBUtil.getDBConn()
        cursor = conn.cursor()
        current_balance = self.get_account_balance(account_number)
        if current_balance >= amount:
            cursor.execute("UPDATE accounts SET balance=balance - ? WHERE acc_no=?", (amount, account_number))
            conn.commit()
            new_balance = self.get_account_balance(account_number)
        else:
            raise ValueError("Insufficient funds")
        cursor.close()
        conn.close()
        return new_balance

    def transfer(self, from_account_number: int, to_account_number: int, amount: float) -> None:
        conn = DBUtil.getDBConn()
        cursor = conn.cursor()
        from_balance = self.get_account_balance(from_account_number)
        if from_balance >= amount:
            cursor.execute("UPDATE accounts SET balance=balance - ? WHERE acc_no=?", (amount, from_account_number))
            cursor.execute("UPDATE accounts SET balance=balance + ? WHERE acc_no=?", (amount, to_account_number))
            conn.commit()
        else:
            raise ValueError("Insufficient funds")
        cursor.close()
        conn.close()

    def get_account_details(self, account_number: int) -> Account:
        conn = DBUtil.getDBConn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM accounts WHERE acc_no=?", (account_number,))
        row = cursor.fetchone()
        customer = self.get_customer_by_id(row[4])  # Fetching customer by id (assuming it's the last column)
        cursor.close()
        conn.close()
        return Account(row[1], row[2], row[3], customer)

    def get_transactions(self, account_number: int, from_date: date, to_date: date) -> List[Transaction]:
        conn = DBUtil.getDBConn()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM transactions
            WHERE account_number=? AND date BETWEEN ? AND ?
        """, (account_number, from_date, to_date))
        rows = cursor.fetchall()
        transactions = [Transaction(row[0], row[1], row[2], row[3], row[4]) for row in rows]
        cursor.close()
        conn.close()
        return transactions

    def get_customer_by_id(self, customer_id: int) -> Customer:
        conn = DBUtil.getDBConn()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customers WHERE id=?", (customer_id,))
        row = cursor.fetchone()
        customer = Customer(row[1], row[2], row[3])
        cursor.close()
        conn.close()
        return customer

    def get_savings_accounts(self):
      conn = DBUtil.get_db_conn()
      cursor = conn.cursor()
      cursor.execute("SELECT account_number, balance, interest_rate FROM accounts WHERE account_type = 'Savings'")
      rows = cursor.fetchall()
      conn.close()
      return rows

    def update_account_balance(self, account_number, new_balance):
       conn = DBUtil.get_db_conn()
       cursor = conn.cursor()
       cursor.execute("UPDATE accounts SET balance = ? WHERE account_number = ?", (new_balance, account_number))
       conn.commit()
       conn.close()

    def get_all_accounts(self):
        conn = DBUtil.getDBConn()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT acc_no, acc_type, balance, customer_id FROM accounts")
            rows = cursor.fetchall()
            accounts = []
            for row in rows:
                acc_no, acc_type, balance, customer_id = row
                # Ideally fetch customer using customer_id
                dummy_customer = Customer("Dummy", "dummy@email.com", "0000000000")
                account = Account(acc_type, balance, dummy_customer)
                account.account_number = acc_no
                accounts.append(account)
            return accounts
        finally:
            cursor.close()
            conn.close()

