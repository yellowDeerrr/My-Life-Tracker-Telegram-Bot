import psycopg2
import configparser

class BotDB:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read("config/config.ini")

        db_host = config.get("database", "host")
        db_port = config.get("database", "port")  # Convert to integer
        db_name = config.get("database", "database")
        db_user = config.get("database", "user")
        db_password = config.get("database", "password")

        try:
            # Connect to PostgreSQL
            self.connection = psycopg2.connect(
                host=db_host,
                port=db_port,
                database=db_name,
                user=db_user,
                password=db_password
            )

            # Create a cursor object
            self.cursor = self.connection.cursor()
        except Exception as e:
            print(f"Error: {e}")



    def get_params_data(self):
        self.cursor.execute("SELECT * FROM params WHERE id=1;")
        rows = self.cursor.fetchall()

        if not rows:
            return "No records found."

        column_names = self._get_column_names()  # Use a helper function
        return self._format_rows(rows, column_names)  # Use a helper function

    def get_params_level_data(self):
        self.cursor.execute("SELECT "
                            '(health,strength,intelligence,wisdom,charisma,confidence,self_discipline,skills,happiness,recovery)'
                            " FROM levels;")
        return self.cursor.fetchone()

    def update_param(self, param, amount : int):
        self.cursor.execute(f'SELECT {param} from params where id = 1;')
        points = self.cursor.fetchone()

        if points[0] + amount >= 100:
            update_new_points_value = points[0] + amount - 100
            self.cursor.execute(f'UPDATE params SET {param} = {update_new_points_value};')
            self.cursor.execute(f'UPDATE levels SET {param} = {param} + 1 where id = 1;')
        else:
            self.cursor.execute(f'UPDATE params SET {param} = {param} + {amount};')

        self.connection.commit()


    def _get_column_names(self):
        """Helper function to get column names from the 'params' table."""
        return [desc[0] for desc in self.cursor.description]


    def _format_rows(self, rows, column_names):
        emoji_map = {
            "health": "❤️",  # Red heart
            "strength": "💪",  # Biceps
            "intelligence": "🧠",  # Brain
            "charisma": "🤩",  # Star-struck
            "self_discipline": "🧘",  # Person in lotus position
            "confidence": "😎",  # Smiling face with sunglasses
            "happiness": "😃",  # Grinning face with big eyes
            "recovery": "🩹",  # Adhesive bandage
            "skills": "🛠️",  # Hammer and wrench
            "wisdom": "🦉",  # Owl
        }
        formatted_output = ""
        for row in rows:
            row_string = ""
            for column_name, value in zip(column_names, row):
                if column_name == "id":
                    continue
                emoji = emoji_map.get(column_name, "❓")  # Get emoji, or use a question mark
                if column_name == 'self_discipline':
                    row_string += f"{emoji} <b>Self Discipline</b>: {value}\n"
                else:
                    row_string += f"{emoji} <b>{column_name.capitalize()}</b>: {value}\n"

                try:
                    percent_parts = int(int(value) / 10)
                    color = "██"
                    row_string += "".join(color for _ in range(percent_parts))
                    row_string += "".join("░░" for _ in range(10 - percent_parts)) + "\n\n"
                except ValueError:
                    row_string += "░░░░░░░░░░\n"
            formatted_output += row_string

        return formatted_output