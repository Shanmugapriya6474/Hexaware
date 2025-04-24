from models.payment import Payment

class PaymentService:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def process_payment(self, payment):
        connection = None
        try:
            connection = self.db_connection.connect()
            with connection.cursor() as cursor:
                # Validate order ID
                cursor.execute("SELECT COUNT(*) FROM orders WHERE order_id = %s", (payment.order_id,))
                if cursor.fetchone()[0] == 0:
                    raise ValueError("Order ID does not exist.")

                # Insert payment transaction
                cursor.execute(
                    "INSERT INTO payments (order_id, payment_method, amount, status) VALUES (%s, %s, %s, %s)",
                    (payment.order_id, payment.payment_method, payment.amount, payment.status)
                )

                # Commit the transaction
                connection.commit()

                # Update order status
                cursor.execute("UPDATE orders SET status = 'Paid' WHERE order_id = %s", (payment.order_id,))
                connection.commit()

                print("Payment processed successfully.")
        except Exception as e:
            connection.rollback()
            print(f"Payment processing failed: {str(e)}")
        finally:
            connection.close()
