from dao.account_dao import AccountDAO
from dao.transaction_dao import TransactionDAO
from entity.transaction import Transaction
from datetime import date


class CustomerServiceProvider:
    def __init__(self):
        self.account_dao = AccountDAO()
        self.transaction_dao = TransactionDAO()

    def get_account_balance(self, account_number):
        account = self.account_dao.get_account(account_number)
        if account:
            return account.get_balance()
        else:
            raise ValueError("Account not found.")

    def deposit(self, account_number, amount):
        account = self.account_dao.get_account(account_number)
        if account:
            account.set_balance(account.get_balance() + amount)
            self.transaction_dao.add_transaction(Transaction(account, "Deposit", "Deposit", amount))
            return account.get_balance()
        else:
            raise ValueError("Account not found.")

    def withdraw(self, account_number, amount):
        account = self.account_dao.get_account(account_number)
        if account:
            if account.get_balance() < amount:
                raise ValueError("Insufficient funds.")
            account.set_balance(account.get_balance() - amount)
            self.transaction_dao.add_transaction(Transaction(account, "Withdrawal", "Withdraw", amount))
            return account.get_balance()
        else:
            raise ValueError("Account not found.")

    def transfer(self, from_account_number, to_account_number, amount):
        from_account = self.account_dao.get_account(from_account_number)
        to_account = self.account_dao.get_account(to_account_number)
        if from_account and to_account:
            if from_account.get_balance() < amount:
                raise ValueError("Insufficient balance.")
            from_account.set_balance(from_account.get_balance() - amount)
            to_account.set_balance(to_account.get_balance() + amount)
            self.transaction_dao.add_transaction(Transaction(from_account, "Transfer", "Transfer", amount))
        else:
            raise ValueError("Invalid account number.")

    def get_account_details(self, account_number):
        return self.account_dao.get_account(account_number)

    def get_transactions(self, account_number, from_date, to_date):
        return self.transaction_dao.get_transactions(account_number, from_date, to_date)
