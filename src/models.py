from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

from db import engine


Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String())
    login = Column(String())
    password = Column(String())
    email = Column(String(120), unique=True)

    def __repr__(self):
        return f"User {self.id}, {self.name}"


def init_db():
    """
    Создаем таблицы из метаданных Base - declarative_base
    Вызывается только один раз при пустой базе
    """
    Base.metadata.create_all(engine)
    
if __name__ == "__main__":
    init_db()