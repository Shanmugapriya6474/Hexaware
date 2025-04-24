from entity.transaction import Transaction


class TransactionDAO:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_transactions(self, account_number, from_date, to_date):
        return [t for t in self.transactions if
                t.get_account().get_account_number() == account_number and from_date <= t.get_date_time().date() <= to_date]
