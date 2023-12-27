from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, mapped_column, Mapped
from app.db import engine

Base = declarative_base()


class User(Base):
    """Пользователи"""

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    login = Column(String)
    password = Column(String)
    email = Column(String(120), unique=True)

    def __repr__(self):
        return f"id: {self.id}, name: {self.name}"


class Outcome(Base):
    __tablename__ = "outcome"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_name = Column(String(255))
    price = Column(Integer)
    quantity = Column(Integer)
    purchase_date = Column(DateTime)


class Income(Base):
    __tablename__ = "income"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    quantity = Column(Integer)
    date = Column(DateTime)


class News(Base):
    __tablename__ = "news"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    text = Column(String)
    date = Column(Date)


def init_db():
    """
    Создаем таблицы из метаданных Base - declarative_base
    Вызывается только один раз при пустой базе
    """
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    init_db()
