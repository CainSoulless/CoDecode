# Flask
from flask import Flask
from flask import redirect
from flask import render_template
from flask import request 
from flask import jsonify
from flask import session
from flask_session import Session
from tempfile import mkdtemp

# Security
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

# SQLITE3
import sqlite3

# helpers
from static.python.helpers import login_required

# Testing
import base64
from time import time

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = sqlite3.connect("database.db", check_same_thread=False)
db.row_factory = sqlite3.Row
cursor = db.cursor()

@app.route("/")
def testing():
    if request.is_json:
        # seconds = time()
        # return jsonify({'seconds': seconds})
        body = request.args.get("message_body")
        print()
        print(body)
        print()
        return jsonify({'body': body})

    return render_template("home.html")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/register", methods=["POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        cursor.execute("SELECT username FROM users WHERE username = ?;", (username,))
        user_exist = cursor.fetchone()

        if not username or not password or user_exist:
            return "error"
        
        cursor.execute("INSERT INTO users (username, hash) VALUES (?, ?);", (username, generate_password_hash(password)))
        db.commit()
        return render_template("home.html")


@app.route("/")
@login_required
def home():
    encrypt_options = [
        "Plain text",
        "base64",
        "SHA-256"
    ] 
    return render_template("home.html", options=encrypt_options)
    # return App.render(render_template("home.html", options=encrypt_options))


@app.route("/login", methods=["GET", "POST"])
def login():

    # Forget any user id
    session.clear()

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            return "Insert valid username and/or password"

        cursor.execute("SELECT * FROM users WHERE username = ?;", (username,))
        row = cursor.fetchone()

        if not check_password_hash(row["hash"], password):
            return "Invalid username or password"

        session["user_id"] = row["id"]

        return redirect("/")

    else:
        return render_template("portal.html")
    

@app.route("/logout", methods=["GET"])
@login_required
def logout():
    session.clear()
    return render_template("portal.html")


if __name__ == "__main__":
    app.run(debug=True)


"""
Thinks to do:
Continuing with AJAX. (https://www.youtube.com/watch?v=nF9riePnm80)
The boostrap was updated, so somethings were broke.
"""