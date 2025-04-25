class Account:
    def __init__(self, account_number, account_type, balance):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += float(amount)
        print(f"₹{amount} deposited. New balance: ₹{self.balance:.2f}")

    def withdraw(self, amount):
        amount = float(amount)
        if self.balance >= amount:
            self.balance -= amount
            print(f"₹{amount} withdrawn. New balance: ₹{self.balance:.2f}")
        else:
            print("Insufficient balance.")

    def calculate_interest(self):
        interest = self.balance * 0.045
        print(f"Interest: ₹{interest:.2f}")
        return interest
