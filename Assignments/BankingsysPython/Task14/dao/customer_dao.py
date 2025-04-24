from entity.customer import Customer


class CustomerDAO:
    def __init__(self):
        self.customers = {}

    def add_customer(self, customer):
        self.customers[customer.get_email()] = customer

    def get_customer(self, email):
        return self.customers.get(email)
