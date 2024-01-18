from datetime import date, timedelta

import pytest
from sqlalchemy.exc import IntegrityError

from app.models import Transaction


@pytest.fixture(
    scope='function',
    params=[
        {'account_id_from': 1, 'transaction_type': 'dept', 'amount': 150, 'date': date.today(),
         'comment': 'test'},
        {'account_id_from': 1, 'transaction_type': 'dept', 'amount': 300, 'date': date.today() - timedelta(1),
         'comment': 'test2'},
    ]
)
def transaction_data_create(request) -> dict:
    return request.param


@pytest.fixture(
    scope='function',
    params=[
        {'id': 1, Transaction.amount: 450},
        {'id': 2, Transaction.comment: 'updated'},
    ]
)
def transaction_data_update(request) -> dict:
    return request.param
