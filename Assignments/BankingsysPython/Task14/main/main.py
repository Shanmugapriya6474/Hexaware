from service.bank_service_provider_impl import BankServiceProviderImpl
from service.customer_service_provider import CustomerServiceProvider
from entity.customer import Customer
from entity.savings_account import SavingsAccount
from entity.current_account import CurrentAccount
from entity.zero_balance_account import ZeroBalanceAccount

def main():

    # --- Example 1: BankServiceProviderImpl demonstration ---
    bank = BankServiceProviderImpl("Chennai Branch", "123 Mount Road")

    # Create customer and accounts
    customer = Customer("Priya", "priya@mail.com", "9876543210")
    acc = bank.create_account(customer, 2001, "Savings", 1000)

    # Deposit, Withdraw and Display Details
    bank.deposit(acc.get_account_number(), 500)
    bank.withdraw(acc.get_account_number(), 300)
    print("Balance:", bank.get_account_balance(acc.get_account_number()))

    # Interest Calculation
    bank.calculate_interest()
    print("Balance after interest:", bank.get_account_balance(acc.get_account_number()))

    # --- Example 2: CustomerServiceProvider demonstration ---
    customer1 = Customer("Jerry", "jerry.d@example.com", "1234567890")

    # Create accounts
    savings_account = SavingsAccount(customer1, 1000, 3.5)
    current_account = CurrentAccount(customer1, 500, 2000)

    # Create service provider
    service_provider = CustomerServiceProvider()

    # Add accounts to DAO
    service_provider.account_dao.add_account(savings_account)
    service_provider.account_dao.add_account(current_account)

    # Perform some operations
    service_provider.deposit(savings_account.get_account_number(), 500)
    print("Savings Account Balance:", service_provider.get_account_balance(savings_account.get_account_number()))

    service_provider.withdraw(current_account.get_account_number(), 100)
    print("Current Account Balance:", service_provider.get_account_balance(current_account.get_account_number()))

    # Transfer between accounts
    service_provider.transfer(savings_account.get_account_number(), current_account.get_account_number(), 200)
    print("Savings Account Balance after Transfer:", service_provider.get_account_balance(savings_account.get_account_number()))
    print("Current Account Balance after Transfer:", service_provider.get_account_balance(current_account.get_account_number()))

if __name__ == "__main__":
    main()
