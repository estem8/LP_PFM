from flask_login import LoginManager
from app.db import Session
from app.db_init import db_init
from app.user.views import blueprint as user_blueprint
from app.edit.edit import edit
from flask import Flask, abort, render_template
from flask import session
import os


def create_app():
    db_init()
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    app.secret_key = os.urandom(32)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(edit, url_prefix='/edit')

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    from app.user.models import User

    @login_manager.user_loader
    def user_loader(user_id) -> User:
        with Session() as db_session:
            return db_session.query(User).get({'id': user_id})

    @app.route("/")
    def index():
        return render_template("home.html")

    @app.route("/profile/<username>")
    def profile(username):
        print(session)
        if "userLogged" not in session or session["userLogged"] != username:
            abort(401)
        return f"Профиль {username}"

    return app
