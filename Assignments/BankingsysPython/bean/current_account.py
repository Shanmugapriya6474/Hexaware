from .account import Account

class CurrentAccount(Account):
    OVERDRAFT_LIMIT = 10000

    def __init__(self, balance, customer):
        super().__init__("Current", balance, customer)

    def withdraw(self, amount):
        if self.balance - amount < -CurrentAccount.OVERDRAFT_LIMIT:
            raise ValueError("Withdrawal exceeds overdraft limit")
        self.balance -= amount
        return self.balance

    def calculate_interest(self):
        return 0.0  # No interest
