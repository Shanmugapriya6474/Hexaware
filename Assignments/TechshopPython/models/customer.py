class Customer:
    def __init__(self, customer_id=None, name=None, email=None, phone=None):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone

    def __repr__(self):
        return f"Customer({self.customer_id}, {self.name}, {self.email}, {self.phone})"
