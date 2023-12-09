from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

from db import engine


Base = declarative_base()

class User(Base):
    """Пользователи"""
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    login = Column(String)
    password = Column(String)
    email = Column(String(120), unique=True)

    def __repr__(self):
        return f'id: {self.id}, name: {self.name}'
    
class News(Base):
    __tablename__='news'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    text = Column(String)


def init_db():
    """
    Создаем таблицы из метаданных Base - declarative_base
    Вызывается только один раз при пустой базе
    """
    Base.metadata.create_all(engine)
    
if __name__ == "__main__":
    init_db()