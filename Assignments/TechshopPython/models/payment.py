class Payment:
    def __init__(self, order_id, payment_method, amount, payment_status):
        self.order_id = order_id
        self.payment_method = payment_method
        self.amount = amount
        self.payment_status = payment_status