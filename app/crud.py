
from flask import flash, redirect, url_for
from sqlalchemy import select
from app.db import Session
from app.models import Account, Transaction
from app.user.models import User
from sqlalchemy import inspect
from sqlalchemy.orm.exc import MultipleResultsFound
from sqlite3 import IntegrityError
from sqlalchemy import exc

def new_user(data):
    new_user = User(data)
    smth = select(User).where(User.login == new_user.login)
    with Session() as session:
        try:
            result = session.execute(smth).one_or_none()
            if result is None:
                session.add(new_user)
                session.commit()
            else:
                flash(f'Пользователь с логином {new_user.login} уже существует')
                return redirect(url_for('user.registration'))    
        except MultipleResultsFound:
            flash(f'Пользователь с логином {new_user.login} уже существует') #скорее всего надо переписать на проверку а не исключение перехватывать
        except exc.IntegrityError:
            flash(f'Ошибка IntegrityError: Скорее всего пользователь с таким email уже существует')
            return redirect(url_for('user.registration'))
        

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
