from db.database_connector import DatabaseConnector

class ReportingDAO:
    @staticmethod
    def get_total_sales_by_date(start_date, end_date):
        try:
            conn = DatabaseConnector.get_connection()
            if conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT OrderDate, SUM(TotalAmount) AS TotalSales
                    FROM Orders
                    WHERE OrderDate BETWEEN ? AND ?
                    GROUP BY OrderDate
                    ORDER BY OrderDate
                """, (start_date, end_date))
                results = cursor.fetchall()
                conn.close()
                return results
        except Exception as e:
            print(f"Error fetching sales report: {e}")
            return []
