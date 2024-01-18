import pytest
from sqlalchemy import Engine, create_engine, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from app.crud import create_or_overrate_transaction, edit_account
from app.models import Base, User


@pytest.fixture()
def engine():
    from app.config import DB_URL
    engine = create_engine(DB_URL, echo=True)
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
    except Exception as e:
        pytest.fail(f"Unexpected error to connect database: {e}")


def test_create_user(db_session: Session):
    '''Тест на запись в бд'''
    user_data = {
        "login": "testuser",
        "password": "testpassword",
        "email": "test@mail"
    }

    user = User(**user_data)
    db_session.add(user)
    db_session.commit()

    #из документации устаревший вариант, наверное не стоит использовать
    # user = db_session.query(User).filter_by(login=login).first()
    assert user.id is not None, "Пользователь не был создан"


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


def test_transaction_create(db_session, transaction_data: dict):
    transaction = create_or_overrate_transaction(db_session, transaction_data)
    assert isinstance(transaction.id, int)


def test_transaction_update(db_session, transaction_data: dict):
    transaction = create_or_overrate_transaction(db_session, transaction_data)
    assert transaction.amount == transaction_data.get('amount')
    if transaction_data.get('id'):
        assert transaction.created_at < transaction.updated_at
