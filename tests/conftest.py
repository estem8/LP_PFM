from datetime import date, timedelta
from http import HTTPStatus

import pytest

from flask.testing import FlaskClient

from app import create_app, db
from app.crud import create_user, delete_obj
from app.models import Transaction


SQLALCHEMY_DATABASE_URI = 'sqlite://'


@pytest.fixture(scope='session')
def app():
    return create_app({
        'SQLALCHEMY_DATABASE_URI': SQLALCHEMY_DATABASE_URI,
        'TESTING': True,
        'DEBUG': True,
        'SERVER_NAME': '0.0.0.0:5000',
        'SECRET_KEY': 'test_secret_key',
        'WTF_CSRF_ENABLED': False,
        'REMEMBER_COOKIE_DURATION': timedelta(days=1),
    })


@pytest.fixture(autouse=True)
def app_ctx(app):
    with app.app_context():
        db.create_all()
        try:
            yield
        finally:
            db.drop_all()


@pytest.fixture
def valid_user():
    return {'login': 'testuser1', 'password': 'testpassword', 'email': 'test@test.com'}


@pytest.fixture
def invalid_user():
    return {'login': 'testuser1', 'password': 'testpassword', 'email': 'test@test.test'}


@pytest.fixture(
    params=[
        {
            'sign_up_data': {'login': 'testuser1', 'password': 'testpassword', 'email': 'test@test.test'},
            'result': {'status_code': HTTPStatus.OK, 'html_content': 'Invalid email address.'}
        },
        {
            'sign_up_data': {'login': 'testuser1', 'password': 'testpassword', 'email': 'test@test.com'},
            'result': {'status_code': HTTPStatus.FOUND,
                       'html_content': '<a href="/users/dashboard">/users/dashboard</a>'}
        }
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


@pytest.fixture()
def valid_user_data(app, valid_user):
    user = create_user(valid_user)
    yield user, valid_user
    delete_obj(user)


@pytest.fixture()
def client(app) -> FlaskClient:
    with app.test_client() as app_client:
        yield app_client

