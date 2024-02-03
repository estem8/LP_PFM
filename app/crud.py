from operator import or_
from typing import Any

from flask_login import current_user
from sqlalchemy import and_, select

from app.common import UserAlreadyExistsError
from app.database import db
from app.models import Account, Transaction, User


def create_user(data: dict[str, Any]) -> User:
    user = db.session.execute(select(User).where(or_(User.login == data['login'], User.email == data['email'])))
    if user.first():
        raise UserAlreadyExistsError
    user = User(data)
    db.session.add(user)
    db.session.commit()
    return user


def delete_obj(obj: db.Model) -> None:
    db.session.delete(obj)
    db.session.commit()
    return


def fetch_accounts(user: User) -> list[Account]:
    return db.session.execute(select(Account).where(Account.user_id == user.id)).scalars().all()


def create_account(name: str, user_id: int, currency: str, symbol=str,) -> Account:
    account = Account(name=name, user_id=user_id, currency=currency, symbol=symbol)

    db.session.add(account)
    db.session.commit()
    return account


def fetch_account(
    account_name: str | None = None,
    account_id: int | None = None,
    user: User | None = None
) -> Account:
    if not any((account_id, account_name)):
        raise Exception('account_id or account_name require')
    user = user if user else current_user
    if account_name:
        return db.session.execute(
            select(Account).where(
                and_(
                    Account.user_id == user.id,
                    Account.name == account_name,
                )
            )
        ).scalars().first()
    return db.session.execute(
            select(Account).where(
                and_(
                    Account.user_id == user.id,
                    Account.id == account_id,
                )
            )
        ).scalars().first()


def create_transaction(transaction_data: dict[str, Any]) -> Transaction:
    transaction = Transaction(
        account_id_from=transaction_data.get('account_id_from'),
        account_id_to=transaction_data.get('account_id_to'),
        transaction_type=transaction_data.get('transaction_type'),
        amount=transaction_data.get('amount'),
        date=transaction_data.get('date'),
        comment=transaction_data.get('comment'),
    )
    db.session.add(transaction)
    db.session.commit()
    return transaction


def update_transaction(tr_id: int, transaction_data: dict[str, Any]) -> Transaction:
    transaction = db.get_or_404(Transaction, tr_id)
    for key, value in transaction_data.items():
        setattr(transaction, key, value)
    db.session.commit()
    return transaction


def user_list():
    return db.session.execute(select(User).order_by(User.username)).scalars()
