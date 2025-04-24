from entity.customer import Customer
from service.bank import Bank



def main():
    bank = Bank()

    while True:
        print("\n---- Banking System Menu ----")
        print("1. Create Account\n2. Deposit\n3. Withdraw\n4. Transfer\n5. Get Balance\n6. Account Details\n7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            cid = input("Customer ID: ")
            fname = input("First Name: ")
            lname = input("Last Name: ")
            email = input("Email: ")
            phone = input("Phone (10 digits): ")
            address = input("Address: ")

            try:
                customer = Customer(cid, fname, lname, email, phone, address)
                customer.set_email(email)
                customer.set_phone(phone)

                acc_type = input("Account Type (Savings/Current): ")
                init_balance = float(input("Initial Balance: "))
                bank.create_account(customer, acc_type, init_balance)
            except ValueError as ve:
                print("Error:", ve)

        elif choice == "2":
            acc_no = int(input("Account Number: "))
            amount = float(input("Amount to deposit: "))
            print("Balance after deposit: ₹", bank.deposit(acc_no, amount))

        elif choice == "3":
            acc_no = int(input("Account Number: "))
            amount = float(input("Amount to withdraw: "))
            try:
                print("Balance after withdrawal: ₹", bank.withdraw(acc_no, amount))
            except ValueError as ve:
                print("Error:", ve)

        elif choice == "4":
            from_acc = int(input("From Account: "))
            to_acc = int(input("To Account: "))
            amount = float(input("Amount to transfer: "))
            try:
                bank.transfer(from_acc, to_acc, amount)
            except ValueError as ve:
                print("Error:", ve)

        elif choice == "5":
            acc_no = int(input("Account Number: "))
            balance = bank.get_account_balance(acc_no)
            if balance is not None:
                print("Current Balance: ₹", balance)
            else:
                print("Account not found.")

        elif choice == "6":
            acc_no = int(input("Account Number: "))
            bank.get_account_details(acc_no)


        elif choice == "7":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
