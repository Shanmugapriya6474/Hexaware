from .icustomer_service_provider import ICustomerServiceProvider

class CustomerServiceProviderImpl(ICustomerServiceProvider):
    def __init__(self):
        self.accounts = {}

    def get_account_by_no(self, acc_no):
        return self.accounts.get(acc_no)

    def get_account_balance(self, acc_no):
        account = self.get_account_by_no(acc_no)
        if account:
            return account.get_balance()
        else:
            raise ValueError("Account not found")

    def deposit(self, acc_no, amount):
        account = self.get_account_by_no(acc_no)
        if account:
            return account.deposit(amount)
        else:
            raise ValueError("Account not found")

    def withdraw(self, acc_no, amount):
        account = self.get_account_by_no(acc_no)
        if account:
            return account.withdraw(amount)
        else:
            raise ValueError("Account not found")

    def transfer(self, from_acc, to_acc, amount):
        from_account = self.get_account_by_no(from_acc)
        to_account = self.get_account_by_no(to_acc)
        if from_account and to_account:
            from_account.withdraw(amount)
            to_account.deposit(amount)
        else:
            raise ValueError("One or both accounts not found")

    def calculate_interest(self, acc_no):
        account = self.get_account_by_no(acc_no)
        if account:
            return account.calculate_interest()
        else:
            raise ValueError("Account not found")
