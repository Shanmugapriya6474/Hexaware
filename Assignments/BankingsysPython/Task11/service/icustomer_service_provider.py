from abc import ABC, abstractmethod

class ICustomerServiceProvider(ABC):

    @abstractmethod
    def get_account_balance(self, acc_no):
        pass

    @abstractmethod
    def deposit(self, acc_no, amount):
        pass

    @abstractmethod
    def withdraw(self, acc_no, amount):
        pass

    @abstractmethod
    def transfer(self, from_acc, to_acc, amount):
        pass

    @abstractmethod
    def calculate_interest(self, acc_no):
        pass
