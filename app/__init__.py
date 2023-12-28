from datetime import datetime
from flask import Flask, abort, render_template, session, redirect, url_for, request
from app.crud import create_user, user_list, edit_transaction, create_news
import os


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.secret_key = os.urandom(32)

    @app.route("/")
    def index():
        return render_template("home.html")

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if "userLogged" in session:
            return redirect(url_for("profile", username=session["userLogged"]))
        elif (
            request.method == "POST"
            and request.form["login"] == "asd"
            and request.form["password"] == "zxc"
        ):
            session["userLogged"] = request.form["login"]
            return redirect(url_for("profile", username=session["userLogged"]))
        return render_template(
            "login.html",
        )

    @app.route("/profile/<username>")
    def profile(username):
        print(session)
        if "userLogged" not in session or session["userLogged"] != username:
            abort(401)

        return f"Профиль {username}"

    @app.route("/signup", methods=["GET", "POST"])
    def register():
        if request.method == "POST":
            username = request.form["login"]
            password = request.form["password"]
            create_user(login=username, password=password)
        return render_template("registration.html")

    @app.route("/edit", methods=["GET", "POST"])
    def edit():
        if request.method == "POST":
            account_id = request.form['account_id']
            transaction_type = request.form['transaction_type']
            amount = request.form['amount']
            date = request.form['date']
            comment = request.form['comment']
            edit_transaction()
        return render_template('edit.html')
 
    return app
