from .ibank_service_provider import IBankServiceProvider
from .customer_service_provider_impl import CustomerServiceProviderImpl
from bean.savings_account import SavingsAccount
from bean.current_account import CurrentAccount
from bean.zero_balance_account import ZeroBalanceAccount

class BankServiceProviderImpl(CustomerServiceProviderImpl, IBankServiceProvider):
    def __init__(self, branch_name="Main Branch", branch_address="City Center"):
        super().__init__()
        self.branch_name = branch_name
        self.branch_address = branch_address

    def create_account(self, customer, acc_type, balance):
        if acc_type.lower() == "savings":
            account = SavingsAccount(balance, customer)
        elif acc_type.lower() == "current":
            account = CurrentAccount(balance, customer)
        elif acc_type.lower() == "zerobalance":
            account = ZeroBalanceAccount(customer)
        else:
            raise ValueError("Invalid account type")

        self.accounts[account.get_acc_no()] = account
        print(f"{acc_type} account created successfully! Account Number: {account.get_acc_no()}")

    def list_accounts(self):
        return list(self.accounts.values())

    def get_account_details(self, acc_no):
        account = self.get_account_by_no(acc_no)
        if account:
            print(account)
        else:
            print("Account not found")

