from operator import or_
from typing import Any

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_, select

from app.common import UserAlreadyExistsError
from app.database import db
from app.models import Account, Transaction, User


def create_user(data: dict[str, Any]) -> User:
    user = db.session.execute(db.select(User).where(or_(User.login == data['login'], User.email == data['email'])))
    if user.first():
        raise UserAlreadyExistsError
    user = User(data)
    db.session.add(user)
    db.session.commit()
    return user


def fetch_accounts(user: User) -> list[Account]:
    return db.session.execute(select(Account).where(Account.user_id == user.id)).scalars().all()


def creat_account(data: dict[str, Any]) -> Account:
    account = Account(**data)
    db.session.add(account)
    db.session.commit()
    return account


def fetch_account(data: dict[str, Any], user: User) -> Account:
    account = Account(**data)
    db.session.execute(
        select(Account).where(
            and_(
                Account.user_id == user.id,
                Account.name == data['name'],
            )
        )
    )
    return account


def create_transaction(transaction_data: dict[str, Any]) -> Transaction:
    transaction = Transaction(**transaction_data)
    db.session.add(transaction)
    db.session.commit()
    return transaction


def update_transaction(tr_id: int, transaction_data: dict[str, Any]) -> Transaction:
    transaction = db.get_or_404(Transaction, tr_id)
    for key, value in transaction_data.items():
        setattr(transaction, key, value)
    db.session.commit()
    return transaction


def user_list(database: SQLAlchemy):
    return database.session.execute(db.select(User).order_by(User.username)).scalars()


"""
# Способ прямого управления сессией. DANGER.
# Надо следить за session.close()
def create_user(login,password):
    session = Session(bind=engine) #Создали сессию
    try:
        new_user = User(login=login,password=password)
        session.add(new_user)
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close() #закрыли сессию

"""
