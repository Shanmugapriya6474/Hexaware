from .account import Account


class CurrentAccount(Account):
    def __init__(self, customer, balance, overdraft_limit):
        super().__init__("Current", balance, customer)
        self.overdraft_limit = overdraft_limit

    def get_overdraft_limit(self):
        return self.overdraft_limit

    def set_overdraft_limit(self, overdraft_limit):
        self.overdraft_limit = overdraft_limit
