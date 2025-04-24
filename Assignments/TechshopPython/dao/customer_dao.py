from db.database_connector import DatabaseConnector
from models.customer import Customer

class CustomerDAO:
    def add_customer(self, customer):
        """Adds a new customer to the database."""
        try:
            connection = DatabaseConnector.get_connection()
            if connection:
                cursor = connection.cursor()
                cursor.execute('''
                    INSERT INTO customers (name, email, phone)
                    VALUES (?, ?, ?)
                ''', (customer.name, customer.email, customer.phone))
                connection.commit()
                connection.close()
        except Exception as e:
            print(f"Error adding customer: {e}")

    def get_customer_by_email(self, email):
        """Retrieves a customer by email to check for duplicates."""
        try:
            connection = DatabaseConnector.get_connection()
            if connection:
                cursor = connection.cursor()
                cursor.execute('''
                    SELECT * FROM customers WHERE email = ?
                ''', (email,))
                customer = cursor.fetchone()
                connection.close()
                return Customer(*customer) if customer else None
        except Exception as e:
            print(f"Error fetching customer: {e}")
            return None

    def update_customer_info(self, customer_id, email=None, phone=None):
        try:
            conn = DatabaseConnector.get_connection()
            if conn:
                cursor = conn.cursor()
                if email:
                    cursor.execute("UPDATE Customers SET Email = ? WHERE CustomerID = ?", (email, customer_id))
                if phone:
                    cursor.execute("UPDATE Customers SET Phone = ? WHERE CustomerID = ?", (phone, customer_id))
                conn.commit()
                conn.close()
                print("Customer information updated successfully.")
        except Exception as e:
            print(f"Error updating customer info: {e}")


    def delete_customer(self, customer_id):
        """Deletes a customer from the database."""
        try:
            connection = DatabaseConnector.get_connection()
            if connection:
                cursor = connection.cursor()
                cursor.execute('''
                    DELETE FROM customers WHERE customer_id = ?
                ''', (customer_id,))
                connection.commit()
                connection.close()
        except Exception as e:
            print(f"Error deleting customer: {e}")
