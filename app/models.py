from typing import List
from datetime import datetime
from sqlalchemy import Column, create_engine, func, ForeignKey, select, Table
from sqlalchemy.orm import declarative_base, mapped_column, Mapped, relationship

from sqlalchemy.orm import sessionmaker
from app.db import engine

Base = declarative_base()

class User(Base):
    """Пользователи"""
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str]
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)

class Account(Base):
    __tablename__ = 'accounts'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    name: Mapped[str]
    currency: Mapped[str]
    symbol: Mapped[str]


class Transaction(Base):
    __tablename__ = 'transactions'
    id: Mapped[int] = mapped_column(primary_key=True)
    account_id: Mapped[int] = mapped_column(ForeignKey('accounts.id'))
    transaction_type: Mapped[str]
    amount: Mapped[int]
    date: Mapped[datetime] = mapped_column(default=func.now())
    comment: Mapped[str]


def init_db():
    """
    Создаем таблицы из метаданных Base - declarative_base
    Вызывается только один раз при пустой базе
    """
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    init_db()
