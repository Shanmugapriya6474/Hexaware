class OverDraftLimitExceededException(Exception):
    def __init__(self, message="Overdraft limit exceeded"):
        self.message = message
        super().__init__(self.message)