from .account import Account

class ZeroBalanceAccount(Account):
    def __init__(self, customer,balance):
        super().__init__('ZeroBalance',balance, customer)
