from abc import ABC, abstractmethod

class Account(ABC):
    last_acc_no = 1000  # Static variable for auto-generating account number

    def __init__(self, acc_type, balance, customer):
        Account.last_acc_no += 1
        self.acc_no = Account.last_acc_no
        self.acc_type = acc_type
        self.balance = balance
        self.customer = customer

    def get_acc_no(self):
        return self.acc_no

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def calculate_interest(self):
        pass

    def __str__(self):
        return f"Account No: {self.acc_no}\nType: {self.acc_type}\nBalance: ₹{self.balance}\n{self.customer}"
