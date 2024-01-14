from datetime import datetime
from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Transaction(Base):
    __tablename__ = 'transactions'
    id: Mapped[int] = mapped_column(primary_key=True)
    account_id_from: Mapped[int] = mapped_column(ForeignKey('accounts.id'))
    account_id_to: Mapped[Optional[int]] = mapped_column(ForeignKey('accounts.id'), nullable=True)
    transaction_type: Mapped[str]
    amount: Mapped[int]
    date: Mapped[datetime]
    comment: Mapped[Optional[str]]
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[Optional[datetime]] = mapped_column(default=datetime.utcnow, onupdate=datetime.utcnow)
    is_deleted: Mapped[bool] = mapped_column(default=False)
