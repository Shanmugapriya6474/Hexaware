class InsufficientFundException(Exception):
    def __init__(self, message="Insufficient funds in the account"):
        self.message = message
        super().__init__(self.message)