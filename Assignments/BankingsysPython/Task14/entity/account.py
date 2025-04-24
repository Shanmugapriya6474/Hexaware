class Account:
    last_acc_no = 1000  # Static variable to generate unique account numbers

    def __init__(self, account_type, balance, customer):
        self.account_number = Account.last_acc_no + 1
        Account.last_acc_no = self.account_number
        self.account_type = account_type
        self.balance = balance
        self.customer = customer

    # Getters and Setters
    def get_account_number(self):
        return self.account_number

    def set_account_number(self, account_number):
        self.account_number = account_number

    def get_account_type(self):
        return self.account_type

    def set_account_type(self, account_type):
        self.account_type = account_type

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        self.balance = balance

    def get_customer(self):
        return self.customer

    def set_customer(self, customer):
        self.customer = customer
