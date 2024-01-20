from datetime import timedelta
import os

basedir = os.path.abspath(os.path.dirname(__file__))
DB_URL = "sqlite:///" + os.path.join(basedir, "..", "webapp.db")

SECRET_KEY = "developer_secret_key"

REMEMBER_COOKIE_DURATION = timedelta(days=14)
