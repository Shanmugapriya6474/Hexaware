
def track_transactions():
    print("\nBank Transaction Tracker")
    transactions = []

    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Exit")
        choice = input("Choose your transaction type: ")

        if choice == '1':
            amount = float(input("Enter deposit amount: ₹"))
            transactions.append(f"Deposited ₹{amount:.2f}")
            print(" Deposit successful.")
        elif choice == '2':
            amount = float(input("Enter withdrawal amount: ₹"))
            transactions.append(f"Withdrew ₹{amount:.2f}")
            print(" Withdrawal successful.")
        elif choice == '3':
            print("\n Transaction History:")
            if not transactions:
                print("No transactions made.")
            else:
                for t in transactions:
                    print("-", t)
            print(" Thank you for using our AK transaction tracker!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
