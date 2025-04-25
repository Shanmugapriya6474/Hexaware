class Account:
    def __init__(self, acc_no, acc_type, balance, customer):
        self.acc_no = acc_no
        self.acc_type = acc_type
        self.balance = balance
        self.customer = customer

    def print_account_info(self):
        print(f"\nAccount No: {self.acc_no}")
        print(f"Type: {self.acc_type}")
        print(f"Balance: ₹{self.balance}")

