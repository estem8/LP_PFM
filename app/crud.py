import logging
from typing import Any

from flask import flash

from app.db import Session
from app.models import Account, Transaction, User


def new_user(data):
    with Session() as session:
        try:
            session.add(User(**data))
            session.commit()
        except Exception as e:
            logging.exception(e)
            flash(f'Пользователь с логином {data["login"]} или почтой {data["email"]} уже существует')


def edit_account(session, user_id, name, currency, symbol):
    account = Account(user_id=user_id, name=name, currency=currency, symbol=symbol)
    session.add(account)
    session.commit()


def create_or_overrate_transaction(
    session,
    transaction_data: dict,
) -> Transaction:
    """
    Создает или обновляет транзакцию.

    Обновляет(перезаписывает), если передан id записи в БД

    :param session:
    :param transaction_data: данные для создания объекта транзакции, который будет записан в БД
    """
    transaction = Transaction(**transaction_data)
    session.add(transaction)
    session.commit()
    return transaction


def new_transaction(transaction_data: dict[str, Any]):
    transaction = Transaction(**transaction_data)
    with Session() as session:
        session.add(transaction)
        session.commit()
        return transaction


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
