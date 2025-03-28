from Database import *

def selectAllFromHistory():
    cursor = connect()
    cursor.execute("SELECT * FROM history")
    return cursor.fetchall()

def selectAllFromParams():
    cursor = connect()
    cursor.execute("SELECT * FROM params")
    return cursor.fetchall()
def addHealth():
    cursor = connect()
    cursor.execute("INSERT INTO params (health) VALUES ()")