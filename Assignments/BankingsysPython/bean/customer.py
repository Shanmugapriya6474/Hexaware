import re

class Customer:
    def __init__(self, customer_id="", first_name="", last_name="", email="", phone="", address=""):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.set_email(email)
        self.set_phone(phone)
        self.address = address

    def set_email(self, email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email format")
        self.email = email

    def set_phone(self, phone):
        if not (phone.isdigit() and len(phone) == 10):
            raise ValueError("Phone number must be 10 digits")
        self.phone = phone

    def __str__(self):
        return (f"Customer ID: {self.customer_id}\nName: {self.first_name} {self.last_name}\n"
                f"Email: {self.email}\nPhone: {self.phone}\nAddress: {self.address}")
