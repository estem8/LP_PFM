import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

engine = create_engine(os.getenv("DB_SQLITE_URL"), echo=True)

"""https://docs.sqlalchemy.org/en/20/orm/session_basics.html#using-a-sessionmaker
что бы избавится от session = Session(bind=engine)
"""
Session = sessionmaker(engine)
Base = declarative_base()
