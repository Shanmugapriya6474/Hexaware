import re

class Customer:
    def __init__(self, cid, fname, lname, email, phone, address):
        self.cid = cid
        self.fname = fname
        self.lname = lname
        self.set_email(email)
        self.set_phone(phone)
        self.address = address

    def set_email(self, email):
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email format.")
        self.email = email

    def set_phone(self, phone):
        if not phone.isdigit() or len(phone) != 10:
            raise ValueError("Invalid phone number.")
        self.phone = phone

    def print_customer_info(self):
        print(f"Customer ID: {self.cid}")
        print(f"Name: {self.fname} {self.lname}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")
        print(f"Address: {self.address}")

