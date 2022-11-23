# Flask
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
import jyserver.Flask as jsf

# Security
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

# SQLITE3
import sqlite3

# helpers
from helpers import login_required

# script.py allocated it static folder
from static.python.script import encrypt

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = sqlite3.connect("database.db", check_same_thread=False)
db.row_factory = sqlite3.Row
cursor = db.cursor()


"""
Jyserver block, modifying the DOM with Python.
"""
@jsf.use(app)
class App:
    def __init__(self):
        self.message = ""
        self.output = ""
        
    
    def input_message(self):
        self.js.document.getElementById("message").innerHTML = self.message
        self.output = encrypt(self.message)


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
        "base64",
        "SHA-256"
    ] 
    # return render_template("home.html")
    return App.render(render_template("home.html", options=encrypt_options))


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
