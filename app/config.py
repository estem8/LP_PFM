from datetime import timedelta
from enum import Enum
from pathlib import Path


BASEDIR = Path(__file__).parent.parent
SQLALCHEMY_DATABASE_URI = f'sqlite:///{Path(BASEDIR, "webapp.db")}'
DB_POOL_SIZE = 20

SECRET_KEY = 'developer_secret_key'

REMEMBER_COOKIE_DURATION = timedelta(days=140)


class TransactionTypeColor(Enum):
    COSTS = '#b41339'
    INCOME = 'green'
    TRANSFER = 'black'
