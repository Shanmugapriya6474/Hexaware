class Product:
    def __init__(self, product_id=None, name=None, price=None, description=None, stock=None):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.description = description
        self.stock = stock

    def __repr__(self):
        return f"Product({self.product_id}, {self.name}, {self.price}, {self.description}, {self.stock})"
