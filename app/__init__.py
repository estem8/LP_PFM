from flask import Flask, abort, render_template, session, request
from app.crud import last_news, create_news
from app.user.views import blueprint as user_blueprint
import os


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    app.secret_key = os.urandom(32)
    app.register_blueprint(user_blueprint)

    @app.route("/")
    def index():
        return render_template("home.html")

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
