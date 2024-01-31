import os

from flask import Flask, abort, render_template, session
from flask_login import LoginManager

from app.database import db
from app.edit.edit import edit
from app.transactions.views import blueprint as transaction_blueprint
from app.user.views import blueprint as user_blueprint


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    app.secret_key = os.urandom(32)
    app.register_blueprint(edit)
    app.register_blueprint(transaction_blueprint)
    app.register_blueprint(user_blueprint)

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    from app.models import User

    @login_manager.user_loader
    def user_loader(user_id) -> User:
        return db.get_or_404(User, user_id)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/profile/<username>')
    def profile(username):
        print(session)
        if 'userLogged' not in session or session['userLogged'] != username:
            abort(401)
        return f'Профиль {username}'

    return app
