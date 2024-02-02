from app import create_app
from app.models import *  # noqa: F403
from app.models import db


def db_init():
    """
    Create the table schema in the database. This requires an application context.
    Since you’re not in a request at this point, create one manually
    Вызывается только один раз при пустой базе
    """
    app = create_app()
    with app.app_context():
        db.create_all()


if __name__ == '__main__':
    db_init()
