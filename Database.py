import psycopg2
import configparser

def connect():
    config = configparser.ConfigParser()
    config.read("config.ini")

    db_host = config.get("database", "host")
    db_port = config.get("database", "port")  # Convert to integer
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

        cursor.execute("""CREATE TABLE params (
                id INT PRIMARY KEY AUTO_INCREMENT,
                Health INT,
                Strength INT,
                Intelligence INT,
                Charisma INT,
                Self_Discipline INT,
                Confidence INT,
                Happiness INT,
                Recovery INT,
                Skills INT,
                Wisdom INT
            )
            """)
        connection.commit()
        cursor.execute("""INSERT INTO params (
                Health,
                Strength,
                Intelligence,
                Charisma,
                Self_Discipline,
                Confidence,
                Happiness,
                Recovery,
                Skills,
                Wisdom
            ) VALUE (10, 10, 10, 10, 10, 10, 10, 10, 10, 10)
            """)
        connection.commit()
        cursor.execute("""CREATE TABLE history (
            id INT PRIMARY KEY AUTO_INCREMENT,
            description TEXT,
            update_param VARCHAR
        );
            """)
        connection.commit()
        return cursor
    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the connection
        if 'connection' in locals() and connection:
            cursor.close()
            connection.close()
            print("Database connection closed.")

