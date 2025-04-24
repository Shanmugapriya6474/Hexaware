class Bank:
    def __init__(self):
        self.accounts = {}  # Using Dictionary (HashMap) to store accounts by account number

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

        self.accounts[account_number] = account  # Store account by account number
        return account

    def get_account_balance(self, acc_no):
        account = self.accounts.get(acc_no)
        if account:
            return account.get_balance()
        else:
            raise InvalidAccountException(f"Account with number {acc_no} not found.")
