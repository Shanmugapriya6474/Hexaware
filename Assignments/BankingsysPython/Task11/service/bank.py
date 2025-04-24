# service/bank.py
from exception.insufficient_fund_exception import InsufficientFundException
from exception.invalid_account_exception import InvalidAccountException
from exception.overdraft_limit_exceeded_exception import OverDraftLimitExceededException
from bean.savings_account import SavingsAccount
from bean.current_account import CurrentAccount
from bean.zero_balance_account import ZeroBalanceAccount

class Bank:
    def __init__(self):
        self.accounts = {}
        self.lastAccNo = 1000  # Starting account number

    def create_account(self, customer, acc_type, balance):
        self.lastAccNo += 1
        account_number = self.lastAccNo

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

        self.accounts[account_number] = account
        return account

    def get_account_balance(self, acc_no):
        account = self.accounts.get(acc_no)
        if account:
            return account.get_balance()
        else:
            raise InvalidAccountException(f"Account with number {acc_no} not found.")

    def deposit(self, acc_no, amount):
        account = self.accounts.get(acc_no)
        if not account:
            raise InvalidAccountException(f"Account with number {acc_no} not found.")
        account.deposit(amount)
        return account.get_balance()

    def withdraw(self, acc_no, amount):
        account = self.accounts.get(acc_no)
        if not account:
            raise InvalidAccountException(f"Account with number {acc_no} not found.")

        # Handle specific withdrawal logic for each account type
        if isinstance(account, SavingsAccount):
            if account.get_balance() < amount:
                raise InsufficientFundException("Not enough funds for withdrawal.")
        elif isinstance(account, CurrentAccount):
            if account.get_balance() + account.get_overdraft_limit() < amount:
                raise OverDraftLimitExceededException("Cannot exceed overdraft limit.")

        account.withdraw(amount)
        return account.get_balance()

    def transfer(self, from_acc_no, to_acc_no, amount):
        from_account = self.accounts.get(from_acc_no)
        to_account = self.accounts.get(to_acc_no)

        if not from_account:
            raise InvalidAccountException(f"Account {from_acc_no} not found.")
        if not to_account:
            raise InvalidAccountException(f"Account {to_acc_no} not found.")

        if isinstance(from_account, SavingsAccount):
            if from_account.get_balance() < amount:
                raise InsufficientFundException("Not enough funds to transfer.")

        # Logic to handle transfer
        from_account.withdraw(amount)
        to_account.deposit(amount)
        return from_account.get_balance(), to_account.get_balance()

    def get_account_details(self, acc_no):
        account = self.accounts.get(acc_no)
        if not account:
            raise InvalidAccountException(f"Account with number {acc_no} not found.")
        return account


