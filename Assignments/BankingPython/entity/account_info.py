
class Account:
    def __init__(self, acc_number=None, acc_type="Savings", balance=0.0):
        self.acc_number = acc_number
        self.acc_type = acc_type
        self.balance = balance

    # Getters and Setters
    def get_acc_number(self): return self.acc_number
    def set_acc_number(self, number): self.acc_number = number

    def get_acc_type(self): return self.acc_type
    def set_acc_type(self, acc_type): self.acc_type = acc_type

    def get_balance(self): return self.balance

    def set_balance(self, balance): self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f" ₹{amount:.2f} deposited successfully. New Balance: ₹{self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f" ₹{amount:.2f} withdrawn successfully. New Balance: ₹{self.balance:.2f}")
        else:
            print(" Insufficient balance.")

    def calculate_interest(self):
        if self.acc_type.lower() == "savings":
            interest = self.balance * 0.045
            self.balance += interest
            print(f"Interest of ₹{interest:.2f} added. New Balance: ₹{self.balance:.2f}")
        else:
            print("Interest not applicable for current accounts.")

    def display_info(self):
        print(f"\n Account Info:\n"
              f"Account Number: {self.acc_number}\n"
              f"Account Type: {self.acc_type}\n"
              f"Balance: ₹{self.balance:.2f}")
