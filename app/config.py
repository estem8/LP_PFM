import os

basedir = os.path.abspath(os.path.dirname(__file__))
DB_URL = "sqlite:///" + os.path.join(basedir, "..", "webapp.db")

SECRET_KEY = "rqwr,_w#@$1412KJ<NIOU8uioLKJlk;kUYTYUk.jGKJHfrtrtybkj,lOIOP"