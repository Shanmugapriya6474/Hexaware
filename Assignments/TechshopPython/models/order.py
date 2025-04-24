class Order:
    def __init__(self, order_id=None, customer_id=None, total_amount=0.0, status="Pending"):
        self.order_id = order_id
        self.customer_id = customer_id
        self.total_amount = total_amount
        self.status = status
