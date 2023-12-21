from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from webapp.config import DB_URL

engine = create_engine(DB_URL, echo=True)

"""https://docs.sqlalchemy.org/en/20/orm/session_basics.html#using-a-sessionmaker
что бы избавится от session = Session(bind=engine)
"""
Session = sessionmaker(engine)