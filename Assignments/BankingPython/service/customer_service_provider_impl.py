from service.customer_service_provider import CustomerServiceProvider
from entity.transaction import Transaction
from datetime import datetime
from typing import List

class CustomerServiceProviderImpl(CustomerServiceProvider):

    def __init__(self):
        super().__init__()

    def get_account_balance(self, account_number):
        account = self.account_dao.get_account(account_number)
        if account:
            return account.get_balance()
        else:
            raise ValueError("Account not found.")

    def deposit(self, account_number, amount):
        # Check if the account exists
        account = None
        for acc in self.accountList:
            if acc.get_account_number() == account_number:
                account = acc
                break

        if account is None:
            raise ValueError("Account not found.")

        # Proceed with the deposit if account is found
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0.")

        account.balance += amount
        return account.balance

    def withdraw(self, account_number, amount):
        account = self.account_dao.get_account(account_number)
        if account:
            if account.get_account_type() == "Savings":
                if account.get_balance() - amount < 500:
                    raise ValueError("Minimum balance of 500 must be maintained in Savings Account.")
            elif account.get_account_type() == "Current":
                if account.get_balance() + account.get_overdraft_limit() < amount:
                    raise ValueError("Exceeds overdraft limit.")
            elif account.get_account_type() == "Zero Balance":
                if account.get_balance() < amount:
                    raise ValueError("Insufficient balance.")
            account.set_balance(account.get_balance() - amount)
            transaction = Transaction(account, "Withdraw", "Withdraw", amount)
            self.transaction_dao.add_transaction(transaction)
            return account.get_balance()
        else:
            raise ValueError("Account not found.")

    def transfer(self, from_account_number, to_account_number, amount):
        from_acc = self.account_dao.get_account(from_account_number)
        to_acc = self.account_dao.get_account(to_account_number)
        if from_acc and to_acc:
            self.withdraw(from_account_number, amount)
            self.deposit(to_account_number, amount)
        else:
            raise ValueError("One or both accounts not found.")

    def get_account_details(self, account_number):
        return self.account_dao.get_account(account_number)

    def get_transactions(self, account_number, from_date, to_date):
        return self.transaction_dao.get_transactions(account_number, from_date, to_date)
