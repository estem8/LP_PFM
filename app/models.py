from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase

class Base(DeclarativeBase):
    pass
"""Правильный способ объявления класса Base
вместо Base = declarative_base()"""
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
