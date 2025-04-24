
class Customer:
    def __init__(self, customer_id=None, first_name="", last_name="", email="", phone="", address=""):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address

    # Getters and Setters
    def get_customer_id(self): return self.customer_id
    def set_customer_id(self, cid): self.customer_id = cid

    def get_first_name(self): return self.first_name
    def set_first_name(self, name): self.first_name = name

    def get_last_name(self): return self.last_name
    def set_last_name(self, name): self.last_name = name

    def get_email(self): return self.email
    def set_email(self, email): self.email = email

    def get_phone(self): return self.phone
    def set_phone(self, phone): self.phone = phone

    def get_address(self): return self.address
    def set_address(self, addr): self.address = addr

    def display_info(self):
        print(f"\n Customer Info:\n"
              f"ID: {self.customer_id}\n"
              f"Name: {self.first_name} {self.last_name}\n"
              f"Email: {self.email}\n"
              f"Phone: {self.phone}\n"
              f"Address: {self.address}")
