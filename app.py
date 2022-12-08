#!/usr/bin/python3

"""
Autor: Rodrigo Hormazabal (aka CainSoulless)
"""

# Flask
from flask import Flask
from flask import jsonify
from flask import redirect
from flask import render_template
from flask import request 
from flask import url_for 
from flask import session
from flask_session import Session

# Security
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

# SQLITE3
import sqlite3

# helpers
from static.python.helpers import login_required

# Encoders
import static.python.encoders as encoders

# AST
import ast

# Email system stored on static folder
import static.python.emailingSystem as email

# Test
from flask import send_file 
from flask import send_from_directory



app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = sqlite3.connect("database.db", check_same_thread=False)
db.row_factory = sqlite3.Row
cursor = db.cursor()


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def home():
    """
    Render the home page where the user can send and/or encode the message.
    """
    cursor.execute("SELECT username FROM users WHERE id = ?;", (session["user_id"],))
    username = cursor.fetchone()

    encoders_options = [
        "Plain text",
        "base64",
        "SHA-256",
        "AES_EAX"
    ] 
    return render_template("home.html", options=encoders_options, username=username["username"])


@app.route("/key-generator", methods=["GET"])
def key_generator():
    """
    Receive an ajax object from handler.js, then generate a random key and
    send it to the front-end without needes of refresh the web-page.
    """
    if request.is_json:
        key_generator = encoders.random_key()
        key_generator = encoders.base64.b64encode(key_generator)
        return jsonify({'key_generator': key_generator.decode("utf-8")})


@app.route("/output-visualization", methods=["POST"])
def output_visualization():
    """
    This is the request an render ajax object sended from Jquery, receive the body and the
    encode option, them render to home.
    """
    if request.is_json:
        if request.method == "POST":
            json_object = ast.literal_eval(request.data.decode("utf-8"))
            message = json_object.get("message")
            encode_option = json_object.get("encode_option")

            if encode_option == "AES_EAX":
                nonce, output, tag = encoders.encode_option(encode_option, message)
            else:
                output = encoders.encode_option(encode_option, message)

            return jsonify({'output': output})
    return redirect("/home")


@app.route("/download", methods=["GET"])
def download_file():
    return send_from_directory("static/files", f"{session['user_id']}-AES.txt", as_attachment=True)


@app.route("/send-email", methods=["POST", "GET"])
def send_email():
    send_from_directory("static/files", f"{session['user_id']}-AES.txt", )
    if request.is_json:
        if request.method == "POST":
            json_object = ast.literal_eval(request.data.decode("utf-8"))
            email_receiver = json_object.get("email_receiver")
            subject = json_object.get("subject")
            encode_option = json_object.get("encode_option")
            key = json_object.get("key")
            message = json_object.get("message")

            if encode_option == "AES_EAX":
                nonce, output, tag = encoders.encode_option(encode_option, message)
                with open(f"static/files/{session['user_id']}-AES.txt", "w+") as file_EAX:
                    content = f"{nonce}\n{tag}"
                    file_EAX.write(content)
                    file_EAX.close()

                    # return redirect(url_for("download_file"))
            else:
                output = encoders.encode_option(encode_option, message)


            email.send_email(email_receiver, subject, output)
            return jsonify({
                "email_receiver": email_receiver,
                "subject": subject,
                "encode_option": encode_option,
                "key": key,
                "message": message
            })
        return redirect("/home")


@app.route("/register", methods=["POST"])
def register():
    """
    Register a new user into the database, previously check if 
    all the inputs are correct and valid.
    """
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


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Provide a login form where the user can get your own account.
    """

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
    """
    The user can logout the account for security purposes.
    """
    session.clear()
    return render_template("portal.html")


if __name__ == "__main__":
    app.run(debug=True)