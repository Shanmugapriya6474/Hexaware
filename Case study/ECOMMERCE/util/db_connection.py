import pyodbc
import configparser

class DBConnection:
    @staticmethod
    def get_connection():
        # Read the database configuration from config.ini
        config = configparser.ConfigParser()
        config.read('dbconfig.ini')

        driver = config['database']['driver']
        server = config['database']['server']
        database = config['database']['database']
        trusted_connection = config['database']['trusted_connection']

        # Create the connection string
        connection_string = f'DRIVER={{{driver}}};SERVER={server};DATABASE={database};Trusted_Connection={trusted_connection}'

        try:
            # Establish the connection to the database
            conn = pyodbc.connect(connection_string)
            print("Database connected successfully!")
            return conn
        except Exception as e:
            print("Error connecting to database:", e)
            return None

if __name__ == "__main__":
    conn = DBConnection.get_connection()
    if conn:
        print("Connection successful!")
    else:
        print("Connection failed!")

