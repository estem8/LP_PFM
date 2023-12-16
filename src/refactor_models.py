import enum
from sqlalchemy import ForeignKey, func
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship
import datetime
from db import engine, Session


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    login: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(30), nullable=False) #для password вроде как надо использовать специальную SHA256
    is_deleted: Mapped[bool] = mapped_column(default=False)

class Accounts(Base):
    __tablename__ = 'accounts'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    currency: Mapped[list['Currencys']] = relationship(back_populates='symbol')####
    account_type: Mapped['Account_Types'] = relationship()
    is_archive: Mapped[bool] = mapped_column(default=False)
    is_take_account: Mapped[bool] = mapped_column(default=False)
    is_saving: Mapped[bool] = mapped_column(default=False)



class acc_type_optional(enum.Enum):
    cash = 'cash'
    card = 'card'
    bank_account = 'bank account'

class Account_Types(Base):
    __tablename__ = 'account_type'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[acc_type_optional]

class Currencys(Base):
    __tablename__ = 'currency'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(10))
    symbol: Mapped['Accounts'] = relationship(back_populates='currency')

class Transactions(Base):
    __tablename__ =  'transaction'
    id: Mapped[int] = mapped_column(primary_key=True)
    account_id: Mapped[int] = mapped_column(ForeignKey('accounts.id'))
    amount: Mapped[int] = mapped_column(default=0)
    transaction_category: Mapped[list['Transaction_Categorys']] = relationship(back_populates='name')
    date: Mapped[datetime.datetime] = mapped_column(server_default=func.now()) #<<< Дата в текущий момент по серверу BD
    account_types: Mapped[list['Account_Types']] = relationship(back_populates='name')
    correspondent: Mapped[str]
    correspondent_account: Mapped[str]
    comment: Mapped[str]

class Transaction_Categorys(Base):
    __tablename__ = 'transaction_category'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)

class Transaction_Types(Base):
    __tablename__ = 'transaction_type'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)


def init_base():
    Base.metadata.create_all(engine)

           
if __name__ == '__main__':
    init_base()

