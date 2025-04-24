from db.database_connector import DatabaseConnector
from models.product import Product

class ProductDAO:
    def add_product(self, product):
        """Adds a new product to the catalog."""
        try:
            connection = DatabaseConnector.get_connection()
            if connection:
                cursor = connection.cursor()
                cursor.execute('''
                    INSERT INTO products (name, price, description, stock)
                    VALUES (?, ?, ?, ?)
                ''', (product.name, product.price, product.description, product.stock))
                connection.commit()
                connection.close()
        except Exception as e:
            print(f"Error adding product: {e}")

    def get_product_by_id(self, product_id):
        """Retrieves a product by its ID."""
        try:
            connection = DatabaseConnector.get_connection()
            if connection:
                cursor = connection.cursor()
                cursor.execute('''
                    SELECT * FROM products WHERE product_id = ?
                ''', (product_id,))
                product = cursor.fetchone()
                connection.close()
                return Product(*product) if product else None
        except Exception as e:
            print(f"Error fetching product: {e}")
            return None

    def update_product(self, product):
        """Updates product information."""
        try:
            connection = DatabaseConnector.get_connection()
            if connection:
                cursor = connection.cursor()
                cursor.execute('''
                    UPDATE products
                    SET name = ?, price = ?, description = ?, stock = ?
                    WHERE product_id = ?
                ''', (product.name, product.price, product.description, product.stock, product.product_id))
                connection.commit()
                connection.close()
        except Exception as e:
            print(f"Error updating product: {e}")

    def delete_product(self, product_id):
        """Deletes a product from the catalog."""
        try:
            connection = DatabaseConnector.get_connection()
            if connection:
                cursor = connection.cursor()
                cursor.execute('''
                    DELETE FROM products WHERE product_id = ?
                ''', (product_id,))
                connection.commit()
                connection.close()
        except Exception as e:
            print(f"Error deleting product: {e}")
