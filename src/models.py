"""
manual
https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/basic_use.html

"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from db import engine

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String())
    password = Column(String())
    login = Column(String())
    email = Column(String(120), unique=True)

    def __repr__(self):
        return f"User {self.id}, {self.name}"

if __name__ == "__main__":
     Base.metadata.create_all(engine)