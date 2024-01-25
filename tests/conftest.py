from datetime import date, timedelta
from pathlib import Path

import pytest

from app import config, create_app, db
from app.models import Transaction


SQLALCHEMY_DATABASE_URI = f'sqlite:///{Path(config.BASEDIR, "webapp_test.db")}'


@pytest.fixture(scope='session')
def app():
    return create_app({'SQLALCHEMY_DATABASE_URI': SQLALCHEMY_DATABASE_URI})


@pytest.fixture(autouse=True)
def app_ctx(app):
    with app.app_context():
        db.create_all()
        try:
            yield
        finally:
            db.drop_all()


@pytest.fixture(
    params=[
        {'login': 'testuser', 'password': 'testpassword', 'email': 'test@mail'},
        {'login': 'testuser1', 'password': 'testpassword', 'email': 'test@mail'},
        {'login': 'testuser', 'password': 'testpassword', 'email': 'test1@mail'},
    ]
)
def user_data_create(request) -> dict:
    return request.param


@pytest.fixture(
    params=[
        [
            {'login': 'testuser', 'password': 'testpassword', 'email': 'test@mail'},
            {'login': 'testuser1', 'password': 'testpassword', 'email': 'test@mail'},
        ],
        [
            {'login': 'testuser', 'password': 'testpassword', 'email': 'test@mail'},
            {'login': 'testuser', 'password': 'testpassword', 'email': 'test1@mail'},
        ],
    ]
)
def user_data_create_double(request) -> dict:
    return request.param


@pytest.fixture(
    params=[
        {'name': 'New Account', 'currency': 'USD', 'symbol': '$'},
        {'name': 'Account2', 'currency': 'RUB', 'symbol': '₽'},
    ]
)
def account_data_create(request) -> dict:
    return request.param


@pytest.fixture(
    scope='function',
    params=[
        {'transaction_type': 'dept', 'amount': 150, 'date': date.today(), 'comment': 'test'},
        {'transaction_type': 'dept', 'amount': 300, 'date': date.today() - timedelta(1), 'comment': 'test2'},
    ],
)
def transaction_data_create(request) -> dict:
    return request.param


@pytest.fixture(
    scope='function',
    params=[
        {'id': 1, Transaction.amount: 450},
        {'id': 2, Transaction.comment: 'updated'},
    ],
)
def transaction_data_update(request) -> dict:
    return request.param
