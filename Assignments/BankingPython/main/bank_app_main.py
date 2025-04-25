from bean.customer import Customer
from service.bank_service_provider_impl import BankServiceProviderImpl

def main():
    bank = BankServiceProviderImpl()

    while True:
        print("\n--- Banking System Menu ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Get Balance")
        print("6. Account Details")
        print("7. List Accounts")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            cust_id = input("Customer ID: ")
            fname = input("First Name: ")
            lname = input("Last Name: ")
            email = input("Email: ")
            phone = input("Phone Number: ")
            address = input("Address: ")

            try:
                customer = Customer(cust_id, fname, lname, email, phone, address)
                acc_type = input("Enter account type (Savings/Current/ZeroBalance): ")
                if acc_type.lower() == "zerobalance":
                    balance = 0
                else:
                    balance = float(input("Initial balance: "))

                bank.create_account(customer, acc_type, balance)
            except ValueError as e:
                print("Error:", e)

        elif choice == "2":
            try:
                acc_no = int(input("Account Number: "))
                amount = float(input("Amount to deposit: "))
                new_bal = bank.deposit(acc_no, amount)
                print(f"New Balance: ₹{new_bal}")
            except ValueError as e:
                print("Error:", e)

        elif choice == "3":
            try:
                acc_no = int(input("Account Number: "))
                amount = float(input("Amount to withdraw: "))
                new_bal = bank.withdraw(acc_no, amount)
                print(f"New Balance: ₹{new_bal}")
            except ValueError as e:
                print("Error:", e)

        elif choice == "4":
            try:
                from_acc = int(input("From Account: "))
                to_acc = int(input("To Account: "))
                amount = float(input("Amount to transfer: "))
                bank.transfer(from_acc, to_acc, amount)
                print("Transfer Successful.")
            except ValueError as e:
                print("Error:", e)

        elif choice == "5":
            try:
                acc_no = int(input("Account Number: "))
                balance = bank.get_account_balance(acc_no)
                print(f"Current Balance: ₹{balance}")
            except ValueError as e:
                print("Error:", e)

        elif choice == "6":
            acc_no = int(input("Account Number: "))
            bank.get_account_details(acc_no)

        elif choice == "7":
            print("\n--- List of Accounts ---")
            for acc in bank.list_accounts():
                print(acc)

        elif choice == "8":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
