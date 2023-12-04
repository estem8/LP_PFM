from settings import DB_URL

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine(DB_URL, echo=True)
db_session = scoped_session(sessionmaker(engine))

