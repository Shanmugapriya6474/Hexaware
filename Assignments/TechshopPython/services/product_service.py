from models.product import Product

class ProductService:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def search_products(self, name=None, category=None):
        try:
            connection = self.db_connection.connect()
            query = "SELECT * FROM products WHERE 1=1"
            params = []
            if name:
                query += " AND product_name LIKE %s"
                params.append(f"%{name}%")
            if category:
                query += " AND category = %s"
                params.append(category)

            with connection.cursor() as cursor:
                cursor.execute(query, tuple(params))
                results = cursor.fetchall()
                return [Product(*result) for result in results]
        except Exception as e:
            print(f"Search failed: {str(e)}")
            return []
        finally:
            self.db_connection.close()

    def recommend_products(self, customer_id):
        try:
            connection = self.db_connection.connect()
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT p.product_id, p.product_name, p.category 
                    FROM products p
                    JOIN order_items oi ON p.product_id = oi.product_id
                    JOIN orders o ON oi.order_id = o.order_id
                    WHERE o.customer_id = %s
                    GROUP BY p.category
                    ORDER BY COUNT(p.category) DESC
                    LIMIT 5
                """, (customer_id,))
                recommendations = cursor.fetchall()
                return [Product(*rec) for rec in recommendations]
        except Exception as e:
            print(f"Recommendation failed: {str(e)}")
            return []
        finally:
            self.db_connection.close()
