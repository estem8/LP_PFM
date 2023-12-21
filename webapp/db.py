from flask import current_app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine(current_app.config['DB_URL'], echo=True)

"""https://docs.sqlalchemy.org/en/20/orm/session_basics.html#using-a-sessionmaker
что бы избавится от session = Session(bind=engine)
"""
Session = sessionmaker(engine)
