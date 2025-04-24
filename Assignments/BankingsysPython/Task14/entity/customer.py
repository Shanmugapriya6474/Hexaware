class Customer:
    def __init__(self, name, email, phone,customer_id=None):
        self.name = name
        self.email = email
        self.phone = phone
        self.customer_id = customer_id

    # Getters and Setters
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone
