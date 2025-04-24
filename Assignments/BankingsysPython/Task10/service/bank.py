from entity.account import Account

class Bank:
    def __init__(self):
        self.accounts = {}
        self.next_account_number = 1001

    def create_account(self, customer, acc_type, balance):
        acc_no = self.next_account_number
        account = Account(acc_no, acc_type, balance, customer)
        self.accounts[acc_no] = account
        self.next_account_number += 1
        print(f" Account created successfully! Account Number: {acc_no}")

    def get_account_balance(self, acc_no):
        account = self.accounts.get(acc_no)
        if account:
            return account.balance
        else:
            return None

    def get_account_details(self, acc_no):
        account = self.accounts.get(acc_no)
        if account:
            account.print_account_info()
            account.customer.print_customer_info()
        else:
            print(" Account not found.")

    def deposit(self, acc_no, amount):
        account = self.accounts.get(acc_no)
        if account:
            account.balance += amount
            return account.balance
        else:
            print(" Account not found.")
            return None

    def withdraw(self, acc_no, amount):
        account = self.accounts.get(acc_no)
        if account:
            if account.balance >= amount:
                account.balance -= amount
                return account.balance
            else:
                raise ValueError("Insufficient funds.")
        else:
            raise ValueError("Account not found.")

    def transfer(self, from_acc, to_acc, amount):
        if from_acc in self.accounts and to_acc in self.accounts:
            if self.accounts[from_acc].balance >= amount:
                self.accounts[from_acc].balance -= amount
                self.accounts[to_acc].balance += amount
                print(" Transfer successful.")
            else:
                raise ValueError(" Insufficient funds for transfer.")
        else:
            raise ValueError(" One or both accounts not found.")


