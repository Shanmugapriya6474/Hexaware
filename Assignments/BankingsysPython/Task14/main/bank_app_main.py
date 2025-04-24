from service.bank_service_provider_impl import BankServiceProviderImpl
from entity.customer import Customer
from entity.zero_balance_account import ZeroBalanceAccount
from entity.savings_account import SavingsAccount
from entity.current_account import CurrentAccount
from exceptions.insufficient_balance_exception import InsufficientBalanceException
from exceptions.account_not_found_exception import AccountNotFoundException


class BankApp:

    def __init__(self):
        self.service_provider = BankServiceProviderImpl("Main Branch", "123 Main Street")

    def run(self):
        while True:
            print("\n----- Welcome to the Royal Banking System -----")
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Get Balance")
            print("5. Transfer")
            print("6. Get Account Details")
            print("7. List Accounts")
            print("8. Get Transactions")
            print("9. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.create_account()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                self.get_balance()
            elif choice == "5":
                self.transfer()
            elif choice == "6":
                self.get_account_details()
            elif choice == "7":
                self.list_accounts()
            elif choice == "8":
                self.get_transactions()
            elif choice == "9":
                print("Thank you for using the banking system.")
                break
            else:
                print("Invalid choice. Please try again.")

    def create_account(self):
        while True:
            print("\nChoose Account Type:")
            print("1. Zero Balance Account")
            print("2. Savings Account")
            print("3. Current Account")
            print("4. Exit to Main Menu")

            acc_choice = input("Enter your choice: ")

            if acc_choice == "4":
                break

            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            phone = input("Enter customer phone: ")
            customer = Customer(name, email, phone)

            acc_no = int(input("Enter desired account number: "))
            balance = float(input("Enter initial balance: "))
            interest_rate = float(input("Enter interest rate: "))
            overdraft_limit = float(input("Enter overdraft limit: "))

            try:
                if acc_choice == "1":
                    account = ZeroBalanceAccount(customer, balance)
                    acc_type = "ZeroBalance"
                elif acc_choice == "2":
                    account = SavingsAccount(customer, balance,interest_rate)
                    acc_type = "Savings"
                elif acc_choice == "3":
                    account = CurrentAccount(customer, balance,overdraft_limit)
                    acc_type = "Current"
                else:
                    print("Invalid option. Try again.")
                    continue

                self.service_provider.create_account(customer, acc_no, acc_type, balance)
                print("Account created successfully!")

            except ValueError as e:
                print(f"Error: {e}")

    def deposit(self):
        try:
            acc_no = int(input("Enter account number: "))
            amount = float(input("Enter amount to deposit: "))
            new_balance = self.service_provider.deposit(acc_no, amount)
            print(f"Deposit successful. New balance: {new_balance}")
        except ValueError as e:
            print(f"Error: {e}")

    def withdraw(self):
        try:
            acc_no = int(input("Enter account number: "))
            amount = float(input("Enter amount to withdraw: "))
            new_balance = self.service_provider.withdraw(acc_no, amount)
            print(f"Withdrawal successful. New balance: {new_balance}")
        except (ValueError, InsufficientBalanceException) as e:
            print(f"Error: {e}")

    def get_balance(self):
        try:
            acc_no = int(input("Enter account number: "))
            balance = self.service_provider.get_balance(acc_no)
            print(f"Current balance: {balance}")
        except ValueError as e:
            print(f"Error: {e}")

    def transfer(self):
        try:
            from_acc = int(input("Enter sender account number: "))
            to_acc = int(input("Enter receiver account number: "))
            amount = float(input("Enter amount to transfer: "))
            self.service_provider.transfer(from_acc, to_acc, amount)
            print("Transfer successful.")
        except (ValueError, InsufficientBalanceException) as e:
            print(f"Error: {e}")

    def get_account_details(self):
        try:
            acc_no = int(input("Enter account number: "))
            account = self.service_provider.get_account_details(acc_no)
            print(f"Account Number: {account.get_account_number()}")
            print(f"Account Type: {account.get_account_type()}")
            print(f"Balance: {account.get_balance()}")
            print(f"Customer Name: {account.customer.get_name()}")
        except (ValueError, AccountNotFoundException) as e:
            print(f"Error: {e}")

    def list_accounts(self):
        accounts = self.service_provider.list_accounts()
        if not accounts:
            print("No accounts found.")
        for acc in accounts:
            print(f"{acc.get_account_number()} - {acc.get_account_type()} - ₹{acc.get_balance()}")

    def get_transactions(self):
        acc_no = int(input("Enter account number: "))
        from_date = input("Enter from date (YYYY-MM-DD): ")
        to_date = input("Enter to date (YYYY-MM-DD): ")
        transactions = self.service_provider.get_transactions(acc_no, from_date, to_date)
        if not transactions:
            print("No transactions found.")
        for txn in transactions:
            print(txn)


if __name__ == "__main__":
    bank_app = BankApp()
    bank_app.run()
