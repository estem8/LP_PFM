from sqlalchemy import Column, Integer, String, ForeignKey, func
from sqlalchemy.orm import declarative_base,mapped_column,Mapped
import datetime
from typing import Annotated
from db import engine


Base = declarative_base()

intpk = Annotated[int, mapped_column(primary_key=True)]


class User(Base):
    """Пользователи"""
    __tablename__ = 'users'
    id: Mapped[intpk] #Для повторяемости кода используется Annotated из typing
    first_name: Mapped[str]
    login: Mapped[str]
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)

    # def __repr__(self):
    #     return f'id: {self.id}, name: {self.name}'
    
class Outcome(Base):
  __tablename__ = 'outcome'
  id: Mapped[int] = mapped_column(primary_key=True)
  user_id:Mapped[int] = mapped_column(ForeignKey('users.id'))
  product_name: Mapped[str]
  price: Mapped[int]
  quantity: Mapped[int]
  purchase_date: Mapped[datetime.datetime]

class Income(Base):
  __tablename__ = 'income'
  id: Mapped[int] = mapped_column(primary_key=True)
  name:Mapped[str]
  quantity: Mapped[int]
  date: Mapped[datetime.datetime]
  
    
class News(Base):
    __tablename__ = 'news'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    text: Mapped[str]
    date: Mapped[datetime.datetime] = mapped_column(server_default=func.now())

def init_db():
    """
    Создаем таблицы из метаданных Base - declarative_base
    Вызывается только один раз при пустой базе
    """
    Base.metadata.create_all(engine)
    
if __name__ == "__main__":
    init_db()