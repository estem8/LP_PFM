import logging

from typing import Any

from flask import flash
from sqlalchemy.exc import DatabaseError

from app.common import DoesNotExist
from app.db import Session
from app.models import Account, Transaction, User


def new_user(data: dict) -> User:
    with Session() as session:
        try:
            user = User(data)
            session.add(user)
            session.commit()
            return user
        except DatabaseError as e:
            logging.exception(e)
            flash(f'Пользователь с логином {data["login"]} или почтой {data["email"]} уже существует')


def edit_account(session, user_id, name, currency, symbol) -> Account:
    account = Account(user_id=user_id, name=name, currency=currency, symbol=symbol)
    session.add(account)
    session.commit()
    return account


def create_transaction(transaction_data: dict[str, Any]) -> Transaction:
    """
    Создает транзакцию.

    :param transaction_data: данные для создания объекта транзакции, который будет записан в БД
    """

    with Session() as session:
        transaction = Transaction(**transaction_data)
        session.add(transaction)
        session.commit()
        return transaction


def update_transaction(tr_id: int, transaction_data: dict[str, Any], db_session: Session = None) -> Transaction:
    if not db_session:
        db_session = Session()
    with db_session:
        transaction = db_session.get(Transaction, tr_id)
        if not transaction:
            raise DoesNotExist(f'Транзакция с id={tr_id} не найдена')
        for key, value in transaction_data.items():
            setattr(transaction, key, value)
        return db_session.get(Transaction, tr_id)


def user_list():
    with Session() as session:
        user_list = session.query(User).all()
        return user_list  # noqa: RET504


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

if __name__ == '__main__':
    pass
