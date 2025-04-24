from entity.account_base_class import Account

class CurrentAccount(Account):
    OVERDRAFT_LIMIT = 5000.0

    def __init__(self, account_number, balance):
        super().__init__(account_number, "Current", balance)

    def withdraw(self, amount):
        amount = float(amount)
        if self.balance - amount >= -self.OVERDRAFT_LIMIT:
            self.balance -= amount
            print(f"₹{amount} withdrawn. New balance: ₹{self.balance:.2f}")
        else:
            print("Overdraft limit exceeded.")
