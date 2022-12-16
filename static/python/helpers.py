from flask import session, redirect
from functools  import wraps

# File naming purposes.
import random

# Database communication
import sqlite3


db = sqlite3.connect("database.db", check_same_thread=False)
db.row_factory = sqlite3.Row
cursor = db.cursor()


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def get_current_username():
    cursor.execute("SELECT username FROM users WHERE id = ?;", (session["user_id"],))
    username = cursor.fetchone()
    return username[0]


def options():
    encoders_options = [
        "Plain text",
        "base64",
        "SHA-256",
        "AES_EAX"
    ] 
    return encoders_options


def create_file(nonce, tag, session_user_id):
    random_number = str(random.randint(999,9999))
    file_name = random_number + ".txt"
    with open(f"static/files/{file_name}", "w+") as file_EAX:
        content = f"{nonce}\n{tag}"
        file_EAX.write(content)
        file_EAX.close()
    cursor.execute("INSERT INTO files_download (id_username, file_name) VALUES(?, ?);", (session_user_id, file_name))
    db.commit()


def validate_file_user(session_user_id):
    """
    Check if the current user has a file linked to download later.
    """
    cursor.execute("SELECT file_name FROM files_download WHERE id_username = ? ORDER BY id DESC LIMIT 1;", (session_user_id, ))
    file_user = cursor.fetchone()

    if not file_user:
        print("file not found. Exit")
        return False
    return file_user["file_name"]

