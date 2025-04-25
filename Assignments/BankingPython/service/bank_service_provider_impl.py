from service.customer_service_provider_impl import CustomerServiceProviderImpl
from service.i_bank_service_provider import IBankServiceProvider
from entity.savings_account import SavingsAccount
from entity.current_account import CurrentAccount
from entity.zero_balance_account import ZeroBalanceAccount
from typing import List
from repository.bank_repository_impl import BankRepositoryImpl
from repository.db_util import DBUtil
from exceptions.account_not_found_exception import AccountNotFoundException


class BankServiceProviderImpl(CustomerServiceProviderImpl, IBankServiceProvider):

    def __init__(self, branch_name: str, branch_address: str):
        super().__init__()
        DBUtil.initialize_database()
        self.bank_repository = BankRepositoryImpl()  # Initialize first
        self.accountList: List = []
        self.transactionList: List = []
        self.branchName = branch_name
        self.branchAddress = branch_address
        self.accountList = self.bank_repository.get_all_accounts()

    def create_account(self, customer, acc_no, acc_type, balance):
        if acc_type.lower() == "savings":
            if balance < 500:
                raise ValueError("Minimum balance for savings account is 500")
            account = SavingsAccount(customer, balance, 3.5)
        elif acc_type.lower() == "current":
            account = CurrentAccount(customer, balance, 2000)
        elif acc_type.lower() == "zerobalance":
            account = ZeroBalanceAccount(customer,balance)
        else:
            raise ValueError("Invalid account type")

        acc_no = account.account_number
        # Save to database instead of in-memory list
        self.bank_repository.create_account(customer, acc_no, acc_type, balance)
        return account

    def list_accounts(self):
        return self.bank_repository.list_accounts()

    def get_account_details(self, account_number):
        for acc in self.accountList:
            if acc.get_account_number() == account_number:
                return acc
        raise AccountNotFoundException()

    def calculate_interest(self):
         savings_accounts = self.bank_repository.get_savings_accounts()

         for acc in savings_accounts:
                acc_number = acc[0]
                balance = acc[1]
                interest_rate = acc[2]

                interest = balance * (interest_rate / 100)
                new_balance = balance + interest

                self.bank_repository.update_account_balance(acc_number, new_balance)
                print(f"Interest of {interest:.2f} added to account {acc_number}. New balance: {new_balance:.2f}")

    def deposit(self, account_number, amount):
          # Refresh the account list from database
       self.accountList = self.bank_repository.get_all_accounts()

       for account in self.accountList:
          if account.get_account_number == account_number:
            new_balance = account["balance"]+ amount
            account.set_balance(new_balance)
            self.bank_repository.update_balance(account["acc_no"], new_balance)
            return new_balance
       raise ValueError("Account not found.")

