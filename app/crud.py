from flask import flash, redirect, url_for
from sqlalchemy import select
from app.db import Session
from app.models import Account, Transaction
from app.user.models import User
import logging

      
def new_user(data):
    with Session() as session:
        try:
            session.add(User(data))
            session.commit()
        except Exception as e:
            logging.exception(e)
            flash(f'Пользователь с логином {data["login"]} или почтой {data["email"]} уже существует')

def edit_account(session, user_id, name, currency, symbol):
    account = Account(user_id=user_id, name=name, currency=currency, symbol=symbol)
    session.add(account)
    session.commit()


def edit_transaction(
    session,
    account_id,
    transaction_type,
    amount,
    date,
    comment,
):
    item = Transaction(
        account_id=account_id,
        transaction_type=transaction_type,
        amount=amount,
        date=date,
        comment=comment,
    )
    session.add(item)
    session.commit()


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
