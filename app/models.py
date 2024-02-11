from datetime import datetime
from decimal import Decimal

from flask_login import UserMixin
from sqlalchemy import DateTime, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from werkzeug.security import check_password_hash, generate_password_hash

from app.common import TransactionsType
from app.database import db


class User(db.Model, UserMixin):
    """Пользователи
    UserMixin нужен для работы flask_login. Добавляет в модель @property:
    - is_active
    - is_authenticated
    - is_anonymous
    и метод get_id"""

    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)

    def __repr__(self):
        return f'User login = {self.login}, email = {self.email}'

    def set_password(self, password: str):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __init__(self, data: dict[str, str]):
        super().__init__()
        for key, value in data.items():
            if key == 'password':
                value = generate_password_hash(value)
            setattr(self, key, value)


class Account(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey(User.id))
    name: Mapped[str]
    currency: Mapped[str]
    symbol: Mapped[str]

    @property
    def balance(self):
        return self._balance


class Transaction(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    account_id: Mapped[int] = mapped_column(ForeignKey(Account.id))
    transaction_type: Mapped[Enum] = mapped_column(Enum(TransactionsType, native_enum=False, create_constraint=False))
    amount: Mapped[Decimal]
    date: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    comment: Mapped[str] = mapped_column(default='')
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.utcnow, onupdate=datetime.utcnow)
    is_deleted: Mapped[bool] = mapped_column(default=False)

    def __repr__(self):
        return (
            f'{self.__class__} id={self.id}, transaction_type=={self.transaction_type}, amount={self.amount}'
            f'date={self.date} created_at={self.created_at} is_deleted={self.is_deleted}'
        )
