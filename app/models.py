from typing import List
from datetime import datetime
from sqlalchemy import Column, create_engine, func, ForeignKey, select, Table
from sqlalchemy.orm import declarative_base, mapped_column, Mapped, relationship

from sqlalchemy.orm import sessionmaker
# from app.db import engine

engine = create_engine('postgresql://user:password@localhost:5432/db', echo=True)
Base = declarative_base()

Session = sessionmaker(engine)

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

def put_in_base():
    with Session() as session:
        Alex1 = User(
            login='Alex1',
            password= 'password1',
            email = '1@asd.asd'
            )
        Alex2 = User(
            login='Alex2',
            password= 'password2',
            email = '2@asd.asd'
            )
        # session.add_all([Alex1, Alex2])
        # session.commit()




    with Session() as session:
        add_account = Account(user_id=1, name= 'Cash', currency='Dollar')
        # session.add(add_account)
        # session.commit()


    with Session() as session:
        add_transaction = Transaction(account_id = 7, transaction_type='out',amount=100, comment='ЖКХ')
        # session.add(add_transaction)
        # session.commit()

        

def get_from_base():
    with Session() as session:
        data = select(User.id)
        session.execute(data)
        # row = session.execute(select(User.login, User.password)).first()
        



if __name__ == "__main__":
    init_db()
    put_in_base()
    # get_from_base()
