class InvalidDataException(Exception):
    """Exception raised for invalid data input."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InsufficientStockException(Exception):
    """Exception raised when there is insufficient stock for an order."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class IncompleteOrderException(Exception):
    """Exception raised when an order is incomplete or missing details."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class PaymentFailedException(Exception):
    """Exception raised when a payment fails."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class IOException(Exception):
    """Exception raised for I/O operations failure (e.g., file errors)."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class SqlException(Exception):
    """Exception raised for SQL query or database connection errors."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ConcurrencyException(Exception):
    """Exception raised for concurrency issues (e.g., simultaneous updates)."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class AuthenticationException(Exception):
    """Exception raised for authentication failures (e.g., invalid login)."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class AuthorizationException(Exception):
    """Exception raised for authorization failures (e.g., unauthorized access)."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


    def authenticate_user(username, password):
            if username != "admin" or password != "password123":
                raise AuthenticationException("Authentication failed: Invalid credentials.")

            print("User authenticated successfully.")

    try:
        authenticate_user("admin", "wrongpassword")
    except AuthenticationException as e:
        print(f"Error: {e}")