class Bank:
    def __init__(self):
        self.accounts = set()  # Using Set to store accounts (avoid duplicates)

    def create_account(self, customer, acc_type, balance):
        account_number = len(self.accounts) + 1  # Simplified account number generation

        if acc_type.lower() == 'savings':
            if balance < 500:
                raise ValueError("Minimum balance for savings account is 500.")
            account = SavingsAccount(account_number, acc_type, balance, customer)
        elif acc_type.lower() == 'current':
            account = CurrentAccount(account_number, acc_type, balance, customer)
        elif acc_type.lower() == 'zero':
            account = ZeroBalanceAccount(account_number, acc_type, balance, customer)
        else:
            raise ValueError("Invalid account type")

        self.accounts.add(account)  # Avoid duplicates
        return account

    def list_accounts(self):
        # Sort accounts based on the customer's name
        return sorted(self.accounts, key=lambda acc: acc.get_customer().get_first_name())
