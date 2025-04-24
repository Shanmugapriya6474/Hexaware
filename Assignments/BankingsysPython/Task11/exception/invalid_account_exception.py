class InvalidAccountException(Exception):
    def __init__(self, message="Account number is invalid"):
        self.message = message
        super().__init__(self.message)