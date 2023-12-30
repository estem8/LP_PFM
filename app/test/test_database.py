from psycopg2 import OperationalError
from sqlalchemy.orm.session import Session
from app.config import DB_URL
import pytest
from sqlalchemy import Engine, create_engine, select
from sqlalchemy.orm import sessionmaker
from app.models import *
from app.crud import create_user, edit_transaction, edit_account
import os

@pytest.fixture()
def engine():
    engine = create_engine(os.getenv('DB_SQLITE_URL'), echo=True)
    Base.metadata.create_all(engine)
    try:
        yield engine
    finally:
        # pass
        Base.metadata.drop_all(engine)

@pytest.fixture()
def db_session(engine: Engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        yield session
    finally:
        session.close()

def test_database_connection(engine: Engine):
    '''Тест на доступность базы'''
    try:
        connection = engine.connect()
        connection.close()
    except OperationalError as e:
        pytest.fail(f"Failed to connect database: {e}")


def test_create_user(db_session: Session):
    '''Тест на запись в бд'''
    login = "testuser"
    password = "testpassword"
    email = "test@mail"

    create_user(db_session, login, password, email)

    #из документации устаревший вариант, наверное не стоит использовать
    # user = db_session.query(User).filter_by(login=login).first()
    user = db_session.execute(select(User).filter(User.login == login)).scalar()
    assert user is not None, "Пользователь не был создан"
    assert user.login == login, "Неправильный логин пользователя"
    assert user.password == password, "Неправильный пароль пользователя"
    assert user.email == email, "Неправильный email пользователя"

def test_duplicate_email(db_session: Session):
    '''Тестирование создания пользователя с дублирующимся email'''
    login = "UserName_1"
    password = "User_Password_1"
    email = "test_unique@mail.com"
    create_user(db_session, login, password, email)

    login = "UserName_2"
    password = "User_Password_2"
    email = "test_unique@mail.com"
    with pytest.raises(ValueError, match=f'Пользователь с email {email} уже существует'):
        create_user(db_session, login, password, email)

def test_account(db_session):
    user_id=1
    name='New Account'
    currency='USD'
    symbol='$'
    edit_account(db_session, user_id, name, currency, symbol)


def test_transaction(db_session):
    account_id = '1'
    transaction_type = 'OUT'
    amount = 100
    date = '12-12-12'
    comment = 'ЖКХ'
    edit_transaction(db_session, account_id, transaction_type, amount, date, comment)
