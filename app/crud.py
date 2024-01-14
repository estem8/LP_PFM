from typing import Any

from app.db import Session
from app.models import Account
from app.transactions.models import Transaction
from app.user.models import User


def create_user(session, login, password, email):
    existing_user = session.query(User).filter_by(email=email).first()
    if existing_user:
        raise ValueError(f'Пользователь с email {email} уже существует')
    else:
        user = User(login=login, email=email)
        user.set_password(password)
        session.add(user)
        session.commit()


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
