import os

basedir = os.path.abspath(os.path.dirname(__file__))
DB_URL = "sqlite:///" + os.path.join(basedir, "..", "webapp.db")
# DB_URL = 'postgresql://user:password@localhost:5432/test_base'
