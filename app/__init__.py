from flask import Flask, abort, render_template, session, redirect, url_for, request

from app.crud import create_user, user_list, last_news, create_news
from app.forms import LoginForm, RegistrationForm

import os


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.secret_key = os.urandom(32)

    @app.route("/")
    def index():
        return render_template("home.html")

    @app.route('/login')
    def login():
        title = "Вход"
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form)

    @app.route("/signup")
    def registration():
        title = "Регистрация"
        reg_form = RegistrationForm()
        return render_template('registration.html', page_title=title, form=reg_form)

    @app.route("/profile/<username>")
    def profile(username):
        print(session)
        if "userLogged" not in session or session["userLogged"] != username:
            abort(401)
        return f"Профиль {username}"

    @app.route("/admin", methods=["GET", "POST"])
    def create_news_text():
        if request.method == "POST":
            title = request.form["title"]
            text = request.form["text"]
            create_news(title=title, text=text)
        return render_template("admin_panel.html", data=last_news())

    return app
