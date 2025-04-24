from .account import Account

class SavingsAccount(Account):
    MIN_BALANCE = 500
    INTEREST_RATE = 0.045

    def __init__(self, balance, customer):
        if balance < SavingsAccount.MIN_BALANCE:
            raise ValueError("Minimum balance for savings account is ₹500")
        super().__init__("Savings", balance, customer)

    def withdraw(self, amount):
        if self.balance - amount < SavingsAccount.MIN_BALANCE:
            raise ValueError("Insufficient funds (Minimum balance must be maintained)")
        self.balance -= amount
        return self.balance

    def calculate_interest(self):
        return self.balance * SavingsAccount.INTEREST_RATE
