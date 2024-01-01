from datetime import datetime

from flask_login import UserMixin
from sqlalchemy import ForeignKey
from sqlalchemy.orm import declarative_base, mapped_column, Mapped
from werkzeug.security import generate_password_hash, check_password_hash

from app.db import engine

Base = declarative_base()


class User(Base, UserMixin):
    """Пользователи"""
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str]
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)

    def __repr__(self):
        return f'user obj login = {self.login}, email = {self.email}'

    def set_passwords(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


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
    date: Mapped[datetime]
    comment: Mapped[str]


def init_db():
    """
    Создаем таблицы из метаданных Base - declarative_base
    Вызывается только один раз при пустой базе
    """
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    init_db()
