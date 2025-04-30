import pyodbc

class DBConnUtil:
    @staticmethod
    def get_connection():
       connection = pyodbc.connect
       (
         'Driver={ODBC Driver 17 forSQL Server};'
         'Server=LAPTOP-SHAN;'
         'Database=CaseStudy;'
         'trusted_connection=yes;'
       )
       return connection
