class SavingsAccount:
    def __init__(self, customer_name, initial_balance, interest_rate, years):
        self.customer_name = customer_name
        self.initial_balance = initial_balance
        self.interest_rate = interest_rate
        self.years = years
        self.future_balance = 0.0

    def calculate_future_balance(self):
        self.future_balance = self.initial_balance * ((1 + self.interest_rate / 100) ** self.years)
        return self.future_balance
