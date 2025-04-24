from datetime import datetime


class Transaction:
    def __init__(self, account, description, transaction_type, transaction_amount):
        self.account = account
        self.description = description
        self.date_time = datetime.now()
        self.transaction_type = transaction_type
        self.transaction_amount = transaction_amount

    # Getters and Setters
    def get_account(self):
        return self.account

    def set_account(self, account):
        self.account = account

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_date_time(self):
        return self.date_time

    def set_date_time(self, date_time):
        self.date_time = date_time

    def get_transaction_type(self):
        return self.transaction_type

    def set_transaction_type(self, transaction_type):
        self.transaction_type = transaction_type

    def get_transaction_amount(self):
        return self.transaction_amount

    def set_transaction_amount(self, transaction_amount):
        self.transaction_amount = transaction_amount
