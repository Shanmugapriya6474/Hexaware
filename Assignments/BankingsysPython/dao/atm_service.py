class ATMService:
    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        print(f"Current balance: ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit successful. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount % 100 == 0 or amount % 500 == 0:
            self.balance -= amount
            print(f"Withdrawal successful. Current balance: {self.balance:.2f}")
        else:
            print("Withdrawal must be in multiples of 100 or 500.")
