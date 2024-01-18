import logging
from typing import Any

from flask import flash
from sqlalchemy.exc import DatabaseError

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


def update_transaction(transaction_data: dict[str, Any]) -> int:
    with Session() as session:
        tr_id = transaction_data.pop('id')
        session.query(Transaction).filter_by(id=tr_id).first()
        row_count = session.query(Transaction).filter(Transaction.id == tr_id
                                                      ).update(**transaction_data, synchronize_session='evaluate')
        return row_count


def user_list():
    with Session() as session:
        user_list = session.query(User).all()
        return user_list


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
