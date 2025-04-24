from entity.bank_account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, account_number="", customer_name="", balance=0.0, interest_rate=4.5):
        super().__init__(account_number, customer_name, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount: float):
        self._balance += amount
        print(f"₹{amount} deposited. New balance: ₹{self._balance:.2f}")

    def withdraw(self, amount: float):
        if self._balance >= amount:
            self._balance -= amount
            print(f"₹{amount} withdrawn. New balance: ₹{self._balance:.2f}")
        else:
            print("Insufficient balance.")

    def calculate_interest(self):
        interest = (self._balance * self.interest_rate) / 100
        self._balance += interest
        print(f"Interest ₹{interest:.2f} added. New balance: ₹{self._balance:.2f}")
