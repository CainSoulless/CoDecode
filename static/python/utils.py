# Flask
from flask import session
from flask import redirect
from flask import render_template 

from functools  import wraps

# File naming purposes.
import random

# Database communication
import sqlite3

# Execute setup.py if the application is not configured.
import os

# decouple for sensitive data
from decouple import config


# db = sqlite3.connect("../db/database.db", check_same_thread=False)
# db.row_factory = sqlite3.Row
# cursor = db.cursor()


def email_credential_configuration():
    try:
        EMAIL_ADDR = config("EMAIL_ADDR")
        EMAIL_PASS = config("EMAIL_PASS")
        return EMAIL_ADDR, EMAIL_PASS
    except:
        print("Cannot find email address/password. \n" +
              "Probably the application is not configured\n")
        os.system("python3 setup/setup.py")


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                            ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def sqlite_connection():
    db = sqlite3.connect("./static/db/database.db", check_same_thread=False)
    db.row_factory = sqlite3.Row
    cursor = db.cursor
    db.close()
    return cursor 


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
    cursor = sqlite_connection()
    cursor.execute("SELECT username FROM users WHERE id = ?;", (session["user_id"],))
    username = cursor.fetchone()

    return username[0]


def options():
    encoders_options = [
        "Plain text",
        "base64",
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
    cursor = sqlite_connection()
    cursor.execute("INSERT INTO files_download (id_username, file_name) VALUES(?, ?);", (session_user_id, file_name))
    # cursor.db.commit()


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