from .account import Account


class SavingsAccount(Account):
    def __init__(self, customer, balance, interest_rate):
        super().__init__("Savings", balance, customer)
        self.interest_rate = interest_rate

    def get_interest_rate(self):
        return self.interest_rate

    def set_interest_rate(self, interest_rate):
        self.interest_rate = interest_rate

