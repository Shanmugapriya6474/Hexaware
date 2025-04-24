class OrderDetail:
    def __init__(self, detail_id=None, order_id=None, product_id=None, quantity=0, price=0.0):
        self.detail_id = detail_id
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.price = price
