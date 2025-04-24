from entity.account_base_class import Account

class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate=4.5):
        super().__init__(account_number, "Savings", balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        print(f"₹{interest:.2f} interest added. New balance: ₹{self.balance:.2f}")
