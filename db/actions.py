from Database import cursor


def selectAllFromHistory():
    cursor.execute("SELECT * FROM history")
    return cursor.fetchall()

def selectAllFromParams():
    cursor.execute("SELECT * FROM params")
    return cursor.fetchall()
def addHealth():
    cursor.execute("INSERT INTO params (health) VALUES ()")