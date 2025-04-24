from db.database_connector import DatabaseConnector
from models.order import Order
from models.order_detail import OrderDetail

class OrderDAO:
    def __init__(self):
        self.connector = DatabaseConnector()

    def place_order(self, order: Order, order_details: list):
        try:
                conn = DatabaseConnector.get_connection()
                if conn:
                    cursor = conn.cursor()

                    # Sample insert query — adjust as needed for your schema
                    cursor.execute('''
                        INSERT INTO Orders (CustomerID, OrderDate, OrderStatus)
                        VALUES (?, ?, ?)
                    ''', (order.customer_id, order.order_date, order.status))

                    conn.commit()
                    conn.close()
                    print("Order placed successfully.")
        except Exception as e:
                print(f"Error placing order: {e}")

    def get_order_status(self, order_id):
        try:
            conn = DatabaseConnector.get_connection()  # ✅ Get connection
            if conn:
                cursor = conn.cursor()

                cursor.execute('''
                    SELECT OrderStatus FROM Orders WHERE OrderID = ?
                ''', (order_id,))

                result = cursor.fetchone()
                conn.close()
                return result[0] if result else "Order not found"
        except Exception as e:
            print(f"Error retrieving order status: {e}")
            return None
