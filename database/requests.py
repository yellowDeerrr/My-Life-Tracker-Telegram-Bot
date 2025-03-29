import psycopg2
import configparser

class BotDB:
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
    emoji_map_history = {
        "add_points": "✅",  # Plus sign
        "reduce_points": "❌",  # Minus sign
        "add_level": "🌱"
        # Add more emojis for other action types
    }
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

    def get_history_data(self):
        self.cursor.execute("SELECT (type, param, amount, description, date, current_param_value) FROM history;")
        rows = self.cursor.fetchall()

        if not rows:
            return "No history found."



        formatted_output = "✅ - Added Points\n❌ - Reduced Points\n🌱 - Increased Level\n\n"
        for row in rows:
            action_type, param, amount, description, date, current_param_value = row
            emoji = self.emoji_map_history.get(action_type, "❓")  # Get emoji, or use a question mark
            formatted_output += (f"{emoji} Date: {date}\n"
                                 f" Changed Param: {param}\n"
                                 f" Amount: {amount}\n"
                                 f" Current value: {current_param_value}\n"
                                 f" Description:  {description}\n\n")

        return formatted_output

    def add_history_record(self, type, param, amount: int, description):
        if type == 'add_level':
            self.cursor.execute(f"""insert into history (type, param, amount, description, current_param_value) values 
                                            ('{type}', '{param}', {amount}, '{description}', (select {param} from levels));""")
        else:
            self.cursor.execute(f"""insert into history (type, param, amount, description, current_param_value) values 
                                ('{type}', '{param}', {amount}, '{description}', (select {param} from params));""")
        self.connection.commit()

    def get_params_data(self):
        self.cursor.execute("SELECT * FROM params WHERE id=1;")
        rows = self.cursor.fetchall()

        if not rows:
            return "No records found."

        column_names = self._get_column_names()  # Use a helper function
        return self._format_rows(rows, column_names)  # Use a helper function


    def get_params_level_data(self):
        self.cursor.execute("SELECT health, strength, intelligence, wisdom, charisma, confidence, self_discipline, skills, happiness, recovery FROM levels;")
        levels = self.cursor.fetchone()

        if not levels:
            return "No level data found."

        level_names = ["health", "strength", "intelligence", "wisdom", "charisma", "confidence", "self_discipline", "skills", "happiness", "recovery"]

        formatted_output = ""

        for name, level in zip(level_names, levels):
            emoji = self.emoji_map.get(name, "❓")
            if name == 'self_discipline':
                formatted_output += f"{emoji}Self Discipline: {level}\n"
            else:
                formatted_output += f"{emoji}{name.capitalize()}: {level} LVL\n"


        return formatted_output

    # def add_to_history(self, description, ):

    def add_points_param(self, param, amount : int, description):
        self.cursor.execute(f'SELECT {param} from params where id = 1;')
        points = self.cursor.fetchone()

        if points[0] + amount >= 100:
            update_new_points_value = points[0] + amount - 100
            self.add_history_record('add_level', param, 1, 'Adding Level')

            self.cursor.execute(f'UPDATE params SET {param} = {update_new_points_value};')
            self.cursor.execute(f'UPDATE levels SET {param} = {param} + 1 where id = 1;')

        else:
            self.cursor.execute(f'UPDATE params SET {param} = {param} + {amount};')

        self.connection.commit()
        self.add_history_record('add_points', param, amount, description)

    def _get_column_names(self):
        """Helper function to get column names from the 'params' table."""
        return [desc[0] for desc in self.cursor.description]


    def _format_rows(self, rows, column_names):

        formatted_output = ""
        for row in rows:
            row_string = ""
            for column_name, value in zip(column_names, row):
                if column_name == "id":
                    continue
                emoji = self.emoji_map.get(column_name, "❓")  # Get emoji, or use a question mark
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