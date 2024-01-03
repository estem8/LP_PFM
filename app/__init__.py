from flask_login import LoginManager, login_user, logout_user

from app.db import Session
from app.models import User
from app.user.forms import LoginForm
from app.user.views import blueprint as user_blueprint
from app.edit.edit import edit
from flask import Flask, abort, render_template, redirect, url_for, flash
from flask import session
import os


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    app.secret_key = os.urandom(32)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(edit, url_prefix='/edit')

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

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

    @app.route('/process-login', methods=['POST'])
    def process_login():
        form = LoginForm()
        if form.validate_on_submit():
            with Session() as session:
                user = session.query(User).filter_by(login=form.username.data).first()
            if user and user.check_password(form.password.data):
                login_user(user, remember=form.remember_me.data)
                flash('Вы успешно авторизовались')
                return redirect(url_for('index'))

        flash('Неверный логин или пароль')
        return redirect(url_for('user.login'))

    @app.route('/logout')
    def logout():
        logout_user()
        flash('Вы успешно разлогинились')
        return redirect(url_for('index'))

    return app
