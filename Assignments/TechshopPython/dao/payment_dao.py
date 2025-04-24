from dao.database_connector import DatabaseConnector

class PaymentDAO:
    def process_payment(self, payment):
        conn = DatabaseConnector.get_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO Payments (order_id, payment_method, amount, payment_status)
                    VALUES (?, ?, ?, ?)
                """, (payment.order_id, payment.payment_method, payment.amount, payment.payment_status))
                conn.commit()
                print("Payment processed successfully.")
            except Exception as e:
                print(f"Error while processing payment: {e}")
            finally:
                conn.close()
