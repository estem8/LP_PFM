from typing import Any

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import DatabaseError

from app.database import DtaBaseUniqError, db
from app.models import Account, Transaction, User


def create_user(data: dict[str, Any]) -> User:
    try:
        user = User(data)
        db.session.add(user)
        db.session.commit()
        return user
    except DatabaseError as e:
        if 'UNIQUE constraint failed' in e.args[0]:
            field = e.args[0].split()[-1].split('.')[-1]
            raise DtaBaseUniqError(f'Пользователь с таким {field} уже существует') from e
        raise


def creat_account(data: dict[str, Any]) -> Account:
    account = Account(**data)
    db.session.add(account)
    db.session.commit()
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
