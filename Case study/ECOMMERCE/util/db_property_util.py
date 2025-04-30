import configparser
import os


class PropertyUtil:
    @staticmethod
    def get_property_string():
        try:
            # Initialize config parser
            config = configparser.ConfigParser()

            # Read the 'dbconfig.ini' file from the parent directory
            config_path = os.path.join(os.path.dirname(__file__), '..', 'dbconfig.ini')
            config.read(config_path)

            # Debugging: Print out sections to ensure it's read correctly
            print("Config file sections:", config.sections())

            # Get the database connection details from the 'database' section
            driver = config.get('database', 'driver')
            server = config.get('database', 'server')
            database = config.get('database', 'database')
            trusted_connection = config.get('database', 'trusted_connection')

            # Construct the connection string
            connection_str = f"mssql+pyodbc://@{server}/{database}?driver={driver}&trusted_connection={trusted_connection}"

            return connection_str

        except KeyError as e:
            print(f"KeyError: Missing section or key in the config file: {e}")
        except Exception as e:
            print("General error:", e)

        return None

if __name__ == "__main__":
    conn_str = PropertyUtil.get_property_string()
    if conn_str:
        print("Connection string generated successfully!")
        print("Connection String:", conn_str)
    else:
        print("Failed to generate connection string.")






