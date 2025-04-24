from db.database_connector import DatabaseConnector
from models.product import Product

class InventoryDAO:
    def __init__(self):
        pass  # No need to initialize a connection here

    def add_product(self, product: Product):
        conn = DatabaseConnector.get_connection()  #
        if conn is None:
            print("Database connection failed.")
            return

        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO products (name, price, description, stock)
                VALUES (?, ?, ?, ?)
            """, (product.name, product.price, product.description, product.stock))
            conn.commit()
            print("Product added to inventory successfully.")
        except Exception as e:
            print(f"Error while adding product: {e}")
            conn.rollback()
        finally:
            conn.close()

    def update_stock(self, product_id: int, new_stock: int):
        conn = DatabaseConnector.get_connection()
        if conn is None:
            print("Unable to connect to the database.")
            return

        try:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE products SET stock = ? WHERE id = ?
            """, (new_stock, product_id))
            conn.commit()
            print("Inventory stock updated.")
        except Exception as e:
            print("Error updating stock:", e)
            conn.rollback()
        finally:
            conn.close()

    def discontinue_product(self, product_id: int):
        conn = DatabaseConnector.get_connection()  # ✅ Ensure conn is defined here
        if conn is None:
            print("❌ Unable to connect to the database.")
            return

        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
            conn.commit()
            print("Product discontinued.")
        except Exception as e:
            print("Error discontinuing product:", e)
            conn.rollback()
        finally:
            conn.close()
