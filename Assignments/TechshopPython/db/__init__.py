import pyodbc

try:
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=LAPTOP-SHAN\\Shanmugapriya;'
        'DATABASE=TechShop3;'
        'Trusted_Connection=yes;'
    )
    print("Connected successfully!")
    conn.close()
except Exception as e:
    print("Connection failed:", e)
