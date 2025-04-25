from abc import ABC, abstractmethod
from entity.customer import Customer
from entity.account import Account
from entity.transaction import Transaction
from typing import List
from datetime import date

class IBankRepository(ABC):

    @abstractmethod
    def create_account(self, customer: Customer, acc_no: int, acc_type: str, balance: float) -> Account:
        """
        Create a new bank account for the given customer with the initial balance and store in the database.
        """
        pass

    @abstractmethod
    def list_accounts(self) -> List[Account]:
        """
        List all accounts in the bank from the database.
        """
        pass

    @abstractmethod
    def calculate_interest(self) -> None:
        """
        Calculate interest based on balance and interest rate and update the database.
        """
        pass

    @abstractmethod
    def get_account_balance(self, account_number: int) -> float:
        """
        Retrieve the balance of an account from the database.
        """
        pass

    @abstractmethod
    def deposit(self, account_number: int, amount: float) -> float:
        """
        Deposit the specified amount into the account. Update new balance in the database and return the new balance.
        """
        pass

    @abstractmethod
    def withdraw(self, account_number: int, amount: float) -> float:
        """
        Withdraw the specified amount from the account. Update new balance in the database and return the new balance.
        """
        pass

    @abstractmethod
    def transfer(self, from_account_number: int, to_account_number: int, amount: float) -> None:
        """
        Transfer money from one account to another. Update new balances in the database.
        """
        pass

    @abstractmethod
    def get_account_details(self, account_number: int) -> Account:
        """
        Retrieve the account and customer details from the database for a given account number.
        """
        pass

    @abstractmethod
    def get_transactions(self, account_number: int, from_date: date, to_date: date) -> List[Transaction]:
        """
        Retrieve the list of transactions for a given account number between two dates from the database.
        """
        pass
