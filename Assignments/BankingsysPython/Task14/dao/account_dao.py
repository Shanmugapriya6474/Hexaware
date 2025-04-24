from entity.account import Account


class AccountDAO:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.get_account_number()] = account

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def update_account(self, account):
        if account.get_account_number() in self.accounts:
            self.accounts[account.get_account_number()] = account
        else:
            raise ValueError("Account not found.")
