from entity.savings_acct_subclass import SavingsAccount
from entity.current_acct_subclass import CurrentAccount

def main():
    print("===  Welcome to the Bank System ===")
    print("Choose Account Type:")
    print("1. Savings Account")
    print("2. Current Account")
    choice = int(input("Enter your choice (1 or 2): "))

    acc_number = input("Enter Account Number: ")
    initial_balance = float(input("Enter Initial Balance: "))

    if choice == 1:
        account = SavingsAccount(acc_number, initial_balance)
    elif choice == 2:
        account = CurrentAccount(acc_number, initial_balance)
    else:
        print("Invalid choice.")
        return

    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Calculate Interest\n4. Exit")
        option = int(input("Enter your option: "))

        if option == 1:
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif option == 2:
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif option == 3:
            account.calculate_interest()
        elif option == 4:
            print("Thank you for using the Bank System.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()