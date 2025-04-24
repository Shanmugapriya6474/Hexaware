from entity.savings_account import SavingsAccount
from entity.current_account import CurrentAccount

def main():
    print("===  Welcome to the Bank System ===")
    print("Choose Account Type:\n1. Savings Account\n2. Current Account")
    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        acc = SavingsAccount(
            account_number=input("Enter Account Number: "),
            customer_name=input("Enter Customer Name: "),
            balance=float(input("Enter Initial Balance: "))
        )
    elif choice == 2:
        acc = CurrentAccount(
            account_number=input("Enter Account Number: "),
            customer_name=input("Enter Customer Name: "),
            balance=float(input("Enter Initial Balance: "))
        )
    else:
        print("Invalid choice.")
        return

    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Calculate Interest\n4. Display Info\n5. Exit")
        option = int(input("Enter your option: "))

        if option == 1:
            amount = float(input("Enter amount to deposit: "))
            acc.deposit(amount)
        elif option == 2:
            amount = float(input("Enter amount to withdraw: "))
            acc.withdraw(amount)
        elif option == 3:
            acc.calculate_interest()
        elif option == 4:
            acc.print_details()
        elif option == 5:
            print(" Thank you for banking with us.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
