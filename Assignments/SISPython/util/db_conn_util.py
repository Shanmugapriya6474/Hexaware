import pyodbc

class DBConnUtil:
    @staticmethod
    def get_connection():
        conn = pyodbc.connect(
           'DRIVER={ODBC Driver 17 for SQL Server};' 
           'SERVER=LAPTOP-SHAN;' 
           'DATABASE=SISDB;' 
           'Trusted_Connection=yes;'
        )
        return conn

# This should be outside the class
try:
    conn = DBConnUtil.get_connection()
    print("Connection successful!")
    conn.close()
except Exception as e:
    print("Connection failed:", e)


       
