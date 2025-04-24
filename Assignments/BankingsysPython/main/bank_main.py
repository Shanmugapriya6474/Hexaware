#Task7
from entity.customer_info import Customer
from entity.account_info import Account

def main():
    # Create customer
    customer = Customer(101, "Shanmugapriya", "R", "shan@gmail.com", "9876543210", "Chennai")
    customer.display_info()

    # Create account
    account = Account("AC7890", "Savings", 5000.0)
    account.display_info()

    # Deposit
    account.deposit(2000.0)

    # Withdraw
    account.withdraw(1000.0)

    # Interest calculation
    account.calculate_interest()

    # Final details
    account.display_info()

if __name__ == "__main__":
    main()
