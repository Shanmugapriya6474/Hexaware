from abc import ABC, abstractmethod
from typing import List
from entity.account import Account
from entity.customer import Customer

class IBankServiceProvider(ABC):

    @abstractmethod
    def create_account(self, customer: Customer, acc_no: int, acc_type: str, balance: float) -> Account:
        pass

    @abstractmethod
    def list_accounts(self) -> List[Account]:
        pass

    @abstractmethod
    def get_account_details(self, account_number: int) -> Account:
        pass

    @abstractmethod
    def calculate_interest(self) -> None:
        pass
