from entity.customer import Customer
from dao.loan_service import LoanService
from dao.atm_service import ATMService
from exception.custom_exception import LoanNotEligibleException
from entity.savings_account import SavingsAccount
from entity.bank_account import BankAccount
from util.password_validator import create_password
from util.transaction_tracker import track_transactions

def main():
    print("=== Loan Eligibility Check ===")
    credit_score = int(input("Enter your credit score: "))
    annual_income = float(input("Enter your annual income: "))
    customer = Customer(credit_score, annual_income)

    loan_service = LoanService()
    try:
        loan_service.check_loan_eligibility(customer)
    except LoanNotEligibleException as e:
        print("Loan Check Failed:", e)

    print("\n=== ATM Transaction ===")
    atm = ATMService(balance=1000.0)

    print("1. Check Balance\n2. Withdraw\n3. Deposit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        atm.check_balance()
    elif choice == 2:
        amount = float(input("Enter amount to withdraw: "))
        atm.withdraw(amount)
    elif choice == 3:
        amount = float(input("Enter amount to deposit: "))
        atm.deposit(amount)
    else:
        print("Invalid choice.")

    calculate_interest_for_customers()
    check_account_balance()
    create_password()#Task5
    track_transactions() #Task6

def calculate_interest_for_customers():
    num_customers = int(input("\nHow many customers to calculate interest for? "))

    customers = []
    for i in range(num_customers):
        print(f"\nEnter details for Customer {i+1}:")
        name = input("Customer Name: ")
        initial_balance = float(input("Initial Balance: "))
        interest_rate = float(input("Annual Interest Rate (%): "))
        years = int(input("Number of Years: "))

        account = SavingsAccount(name, initial_balance, interest_rate, years)
        account.calculate_future_balance()
        customers.append(account)

    print("\n Future Balances for Customers:")
    for customer in customers:
        print(f"{customer.customer_name}: ₹{customer.future_balance:.2f}")


def check_account_balance():
    print("\n Bank Account Balance Checker")

    # Predefined customer accounts (simulate data from DB)
    accounts = [
        BankAccount("ACC1001", "Abi", 3500.00),
        BankAccount("ACC1002", "Bala", 4200.50),
        BankAccount("ACC1003", "Sam", 2950.75),
        BankAccount("ACC1004", "Divya", 8900.00),
    ]

    account_map = {acc.account_number: acc for acc in accounts}

    while True:
        entered_acc = input("\nEnter your account number (or 'exit' to quit): ").strip()

        if entered_acc.lower() == 'exit':
            print("Exiting account balance checker.")
            break

        if entered_acc in account_map:
            acc = account_map[entered_acc]
            print(f"Hello {acc.customer_name}, your account balance is:₹{acc.balance:.2f}")
            break
        else:
            print(" Invalid account number. Please try again.")



if __name__ == "__main__":
    main()
