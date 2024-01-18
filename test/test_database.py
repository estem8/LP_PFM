import pytest
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from app.crud import edit_account
from app.models import Base, User, Transaction


@pytest.fixture(scope='module')  # вызывается единожды при загрузке модуля для всего модуля доступна всегда
def engine():
    from app.config import DB_URL
    engine = create_engine(f'{DB_URL[:-3]}_test.db', echo=True)
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)


@pytest.fixture(scope='module')
def db_session(engine: Engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.rollback()
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

    # из документации устаревший вариант, наверное не стоит использовать
    # user = db_session.query(User).filter_by(login=login).first()
    assert user.id is not None, "Пользователь не был создан"


# def test_duplicate_email(db_session: Session):
#     '''Тестирование создания пользователя с дублирующимся email'''
#     login = "UserName_1"
#     password = "User_Password_1"
#     email = "test_unique@mail.com"
#     create_user(db_session, login, password, email)
#
#     login = "UserName_2"
#     password = "User_Password_2"
#     email = "test_unique@mail.com"
#
#     with pytest.raises(ValueError, match=f'Пользователь с email {email} уже существует'):
#         create_user(db_session, login, password, email)


def test_account(db_session):
    user_id = 1
    name = 'New Account'
    currency = 'USD'
    symbol = '$'
    account = edit_account(db_session, user_id, name, currency, symbol)
    assert account.id, 'Счет не был создан'


def test_transaction_create(transaction_data_create: dict, db_session: Session):
    transaction = Transaction(**transaction_data_create)
    db_session.add(transaction)
    db_session.commit()
    assert transaction.id, 'Транзакция не создана'
