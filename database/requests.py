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
            connection = psycopg2.connect(
                host=db_host,
                port=db_port,
                database=db_name,
                user=db_user,
                password=db_password
            )

            # Create a cursor object
            self.cursor = connection.cursor()
        except Exception as e:
            print(f"Error: {e}")



    def get_params_data(self):
        """
        Retrieves all data from the 'params' table and formats it as a string.

        Returns:
            str: Formatted string of data, or "No records found." if table is empty.
        """
        self.cursor.execute("SELECT * FROM params;")
        rows = self.cursor.fetchall()

        if not rows:
            return "No records found."

        column_names = self._get_column_names()  # Use a helper function
        return self._format_rows(rows, column_names)  # Use a helper function

    def _get_column_names(self):
        """Helper function to get column names from the 'params' table."""
        return [desc[0] for desc in self.cursor.description]

    # def _format_rows(self, rows, column_names):
    #     """Helper function to format rows into a readable string with space between rows."""
    #     formatted_output = ""
    #     for row in rows:
    #         row_string = ""
    #         for column_name, value in zip(column_names, row):
    #             if column_name == "id":
    #                 continue
    #             row_string += f"<b>{column_name.capitalize()}</b>: {value}\n"  # Bold column name using <b> tag
    #             try:
    #                 percent_parts = int(int(value) / 5)
    #                 for i in range(percent_parts):
    #                     row_string += "⬜️"
    #                 for i in range(20 - percent_parts):
    #                     row_string += "░░"
    #                 row_string += "\n\n"
    #             except ValueError:
    #                 row_string += "[░░░░░░░░░░]\n"
    #
    #         formatted_output += row_string + "\n\n"  # Add TWO extra newlines here!
    #     return formatted_output

    # def _format_rows(self, rows, column_names):
    #     """Helper function to format rows into colored progress bars."""
    #     color_map = {
    #         "health": "🔴",  # Red circle
    #         "strength": "🟢",  # Green circle
    #         "intelligence": "🔵",  # Blue circle
    #         "charisma": "🟡",  # Yellow circle
    #         "self_discipline": "🟠",  # Orange circle
    #         "confidence": "🟣",  # Purple circle
    #         "happiness": "🟢",
    #         "recovery": "🔵",
    #         "skills": "🟡",
    #         "wisdom": "🟠",
    #     }
    #     formatted_output = ""
    #     for row in rows:
    #         row_string = ""
    #         for column_name, value in zip(column_names, row):
    #             if column_name != "id":
    #                 row_string += f"<b>{column_name.capitalize()}</b>: {value}\n"
    #                 try:
    #                     percent_parts = int(int(value) / 5)
    #                     color = color_map.get(column_name, "️")  # get color, or default white.
    #                     for i in range(percent_parts):
    #                         row_string += color
    #                     for i in range(20 - percent_parts):
    #                         row_string += "⚫️"
    #                     row_string += "\n"
    #                 except ValueError:
    #                     row_string += "[⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪]\n"
    #
    #         formatted_output += row_string + "\n\n"
    #     return formatted_output

    # def _format_rows(self, rows, column_names):
    #     """Helper function to format rows into colored progress bars."""
    #     color_map = {
    #         "health": "🟥",
    #         "strength": "🟥",
    #         "intelligence": "🟦", # 🟪
    #         "charisma": "🟧",
    #         "self_discipline": "🟨",
    #         "confidence": "🟧",
    #         "happiness": "🟩",
    #         "recovery": "🟩",
    #         "skills": "🟨",
    #         "wisdom": "🟦",
    #     }
    #     formatted_output = ""
    #     for row in rows:
    #         row_string = ""
    #         for column_name, value in zip(column_names, row):
    #             if column_name != "id":
    #                 row_string += f"<b>{column_name.capitalize()}</b>: {value}\n"
    #                 try:
    #                     percent_parts = int(int(value) / 5)
    #                     color = color_map.get(column_name, "⬛️")  # get color, or default space.
    #                     for i in range(percent_parts):
    #                         row_string += color
    #                     for i in range(20 - percent_parts):
    #                         row_string += "░░"  # use space instead of white.
    #                     row_string += "\n\n"
    #                 except ValueError:
    #                     row_string += "[▢▢▢▢▢▢▢▢▢▢▢▢▢▢▢▢▢▢▢▢]\n"  # all empty progress bar.
    #         reordered_columns = ["wisdom", "strength", "intelligence", "charisma", "self_discipline", "confidence",
    #                              "happiness", "recovery", "skills", "health"]
    #         for col in reordered_columns:
    #             if col in lines:
    #                 formatted_output += lines[col]
    #         formatted_output += row_string + "\n\n"
    #     return formatted_output
    # def _format_rows(self, rows, column_names):
    #     """Helper function to format rows with reordered output."""
    #     emoji_map = {
    #         "health": "❤️",  # Red heart
    #         "strength": "💪",  # Biceps
    #         "intelligence": "🧠",  # Brain
    #         "charisma": "🤩",  # Star-struck
    #         "self_discipline": "🧘",  # Person in lotus position
    #         "confidence": "😎",  # Smiling face with sunglasses
    #         "happiness": "😃",  # Grinning face with big eyes
    #         "recovery": "🩹",  # Adhesive bandage
    #         "skills": "🛠️",  # Hammer and wrench
    #         "wisdom": "🦉",  # Owl
    #     }
    #     formatted_output = "\n"
    #     for row in rows:
    #         lines = {}  # Store lines in a dictionary
    #         for column_name, value in zip(column_names, row):
    #             if column_name != "id":
    #                 emoji = emoji_map.get(column_name, "❓")  # Get emoji, or use a question mark
    #                 line = f"{emoji} <b>{column_name.capitalize()}</b>: {value}\n"
    #                 try:
    #                     percent_parts = int(int(value) / 10)
    #                     color = "██"
    #                     line += "".join(color for _ in range(percent_parts))
    #                     line += "".join("░░" for _ in range(10 - percent_parts)) + "\n-\n"
    #                 except ValueError:
    #                     line += "░░░░░░░░░░\n"
    #                 lines[column_name] = line
    #
    #         # Rearrange the lines
    #         reordered_columns = [
    #             "health",
    #             "strength",
    #             "intelligence",
    #             "wisdom",
    #             "charisma",
    #             "confidence",
    #             "self_discipline",
    #             "skills",
    #             "happiness",
    #             "recovery"]
    #         for col in reordered_columns:
    #             if col in lines:
    #                 formatted_output += lines[col]
    #
    #         formatted_output += "\n"
    #     return formatted_output


    def _format_rows(self, rows, column_names):
        #     for row in rows:
        #         row_string = ""
        #         for column_name, value in zip(column_names, row):
        #             if column_name == "id":
        #                 continue
        #             row_string += f"<b>{column_name.capitalize()}</b>: {value}\n"  # Bold column name using <b> tag
        #             try:
        #                 percent_parts = int(int(value) / 5)
        #                 for i in range(percent_parts):
        #                     row_string += "⬜️"
        #                 for i in range(20 - percent_parts):
        #                     row_string += "░░"
        #                 row_string += "\n\n"
        #             except ValueError:
        #                 row_string += "[░░░░░░░░░░]\n"
        #
        #         formatted_output += row_string + "\n\n"  # Add TWO extra newlines here!
        #     return formatted_output
        """Helper function to format rows with reordered output."""
        emoji_map = {
            "health": "❤️",  # Red heart
            "strength": "💪",  # Biceps
            "intelligence": "🧠",  # Brain
            "charisma": "🤩",  # Star-struck
            "self discipline": "🧘",  # Person in lotus position
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
                row_string += f"{emoji} <b>{column_name.capitalize()}</b>: {value}\n"
                try:
                    percent_parts = int(int(value) / 10)
                    color = "██"
                    row_string += "".join(color for _ in range(percent_parts))
                    row_string += "".join("░░" for _ in range(10 - percent_parts)) + "\n-\n"
                except ValueError:
                    row_string += "░░░░░░░░░░\n"
            formatted_output += row_string
            #         for column_name, value in zip(column_names, row):
            #             if column_name == "id":
            #                 continue
            #             row_string += f"<b>{column_name.capitalize()}</b>: {value}\n"  # Bold column name using <b> tag
            #             try:
            #                 percent_parts = int(int(value) / 5)
            #                 for i in range(percent_parts):
            #                     row_string += "⬜️"
            #                 for i in range(20 - percent_parts):
            #                     row_string += "░░"
            #                 row_string += "\n\n"
            #             except ValueError:
            #                 row_string += "[░░░░░░░░░░]\n"
            #
            #         formatted_output += row_string + "\n\n"  # Add TWO extra newlines here!

            # Rearrange the lines
            # reordered_columns = [
            #     "health",
            #     "strength",
            #     "intelligence",
            #     "wisdom",
            #     "charisma",
            #     "confidence",
            #     "self_discipline",
            #     "skills",
            #     "happiness",
            #     "recovery"]
            # for col in reordered_columns:
            #     if col in lines:
            #         formatted_output += lines[col]


        return formatted_output