class AccountNotFoundException(Exception):
    def __init__(self, message="Account not found."):
        super().__init__(message)
