from flask import Flask, redirect, render_template, url_for
from flask_login import LoginManager, current_user

from app.account.views import blueprint as account_blueprint
from app.database import db
from app.edit.views import edit
from app.lk.views import blueprint as lk_blueprint
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

    app.register_blueprint(account_blueprint)
    app.register_blueprint(edit)
    app.register_blueprint(lk_blueprint)
    app.register_blueprint(transaction_blueprint)
    app.register_blueprint(user_blueprint)

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'

    from app.models import User

    @login_manager.user_loader
    def user_loader(user_id) -> User:
        return db.get_or_404(User, user_id)

    @app.route('/')
    def index():
        if current_user.is_authenticated:
            return redirect(url_for('lk.get_lk_page'))
        return render_template('index.html')

    return app
