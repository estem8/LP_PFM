from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app import config

engine = create_engine(config.DB_URL, echo=True, pool_size=config.DB_POOL_SIZE)

"""https://docs.sqlalchemy.org/en/20/orm/session_basics.html#using-a-sessionmaker
что бы избавится от session = Session(bind=engine)
"""
Session = sessionmaker(engine)
