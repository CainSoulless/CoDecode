# Database communication
import sqlite3


db = sqlite3.connect("database.db", check_same_thread=False)
db.row_factory = sqlite3.Row
cursor = db.cursor()

def get_current_username():
    cursor.execute("SELECT username FROM users WHERE id = ?;", (1,))
    username = cursor.fetchone()
    return username[0]

get_current_username()