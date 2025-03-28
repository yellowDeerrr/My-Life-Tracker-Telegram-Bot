import psycopg2
import configparser

config = configparser.ConfigParser()
config.read("../config.ini")

db_host = config.get("database", "host")
db_port = config.getint("database", "port")  # Convert to integer
db_name = config.get("database", "database")
db_user = config.get("database", "user")
db_password = config.get("database", "password")

try:
    # Connect to PostgreSQL
    connection = psycopg2.connect(
        host=db_host,
        port=db_port,
        database=db_name,
        user=db_user,
        password=db_password
    )

    # Create a cursor object
    cursor = connection.cursor()

    # Execute a test query
    cursor.execute("SELECT version();")

    # Fetch and print result
    db_version = cursor.fetchone()
    print(f"Connected to database: {db_version}")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the connection
    if 'connection' in locals() and connection:
        cursor.close()
        connection.close()
        print("Database connection closed.")