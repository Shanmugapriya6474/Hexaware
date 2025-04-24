from entity.bank_account import BankAccount

class CurrentAccount(BankAccount):
    OVERDRAFT_LIMIT = 5000.0

    def deposit(self, amount: float):
        self._balance += amount
        print(f"₹{amount} deposited. New balance: ₹{self._balance:.2f}")

    def withdraw(self, amount: float):
        if self._balance - amount >= -self.OVERDRAFT_LIMIT:
            self._balance -= amount
            print(f"₹{amount} withdrawn. New balance: ₹{self._balance:.2f}")
        else:
            print(" Overdraft limit exceeded.")

    def calculate_interest(self):
        print(" No interest for Current Accounts.")
