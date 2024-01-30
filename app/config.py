from datetime import timedelta
from pathlib import Path


BASEDIR = Path(__file__).parent.parent
SQLALCHEMY_DATABASE_URI = f'sqlite:///{Path(BASEDIR, "webapp.db")}'
DB_POOL_SIZE = 20

OPER_TYPE_CARD_DEPT = 'dept'  # код расходной операции. т.к. в БД нет таблицы с типами операций, то оно живет тут

SECRET_KEY = 'developer_secret_key'

REMEMBER_COOKIE_DURATION = timedelta(days=140)
