from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, account_number="", customer_name="", balance=0.0):
        self._account_number = account_number
        self._customer_name = customer_name
        self._balance = balance

    def get_account_number(self):
        return self._account_number

    def get_customer_name(self):
        return self._customer_name

    def get_balance(self):
        return self._balance

    def set_balance(self, balance):
        self._balance = balance

    def print_details(self):
        print(f"Account No: {self._account_number}, Name: {self._customer_name}, Balance: ₹{self._balance:.2f}")

    @abstractmethod
    def deposit(self, amount: float):
        pass

    @abstractmethod
    def withdraw(self, amount: float):
        pass

    @abstractmethod
    def calculate_interest(self):
        pass
