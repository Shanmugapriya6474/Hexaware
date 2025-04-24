# db/database_connector.py
import pyodbc

class DatabaseConnector:
    @staticmethod
    def get_connection():
        try:
            connection = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};'
                'SERVER=LAPTOP-SHAN;'  # Use your SQL Server name
                'DATABASE=TechShop3;'
                'Trusted_Connection=yes;'
            )
            return connection
        except Exception as e:
            print("Database connection error:", e)
            return None

