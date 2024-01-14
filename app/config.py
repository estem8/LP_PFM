import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))
DB_URL = "sqlite:///" + os.path.join(basedir, "..", "webapp.db")
DB_POOL_SIZE = 20

OPER_TYPE_CARD_DEPT = (
    'dept'  # код расходной операции. т.к. в БД нет таблицы с типами операций, то оно живет тут
)

SECRET_KEY = "rqwr,_w#@$1412KJ<NIOU8uioLKJlk;kUYTYUk.jGKJHfrtrtybkj,lOIOP"

REMEMBER_COOKIE_DURATION = timedelta(days=14)
