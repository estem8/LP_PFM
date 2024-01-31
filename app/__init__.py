from flask import Flask, render_template
from flask_login import LoginManager, current_user, login_required

from app.database import db
from app.edit.views import edit
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

    app.secret_key = app.config['SECRET_KEY']
    app.register_blueprint(edit)
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
        return render_template('index.html')

    @app.route('/profile/')
    @login_required
    def profile():
        return f'Профиль {current_user.__dict__} {dir(current_user)}'

    return app
