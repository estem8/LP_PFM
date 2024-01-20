import pytest
from sqlalchemy import Engine, create_engine, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from app.crud import edit_account, update_transaction, new_user
from app.models import Base, Transaction, User


@pytest.fixture
def engine():
    from app.config import DB_URL
    engine = create_engine(f'{DB_URL[:-3]}_test.db', echo=True)
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)


@pytest.fixture
def db_session(engine: Engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.rollback()
    session.close()


def test_database_connection(engine: Engine):
    """Тест на доступность базы"""
    try:
        connection = engine.connect()
        connection.close()
    except Exception as e:
        pytest.fail(f"Unexpected error to connect database: {e}")


@pytest.fixture
def test_create_user(db_session: Session):
    """Тест на запись в бд"""
    user_data = {
        "login": "testuser",
        "password": "testpassword",
        "email": "test@mail"
    }

    user = User(user_data)
    db_session.add(user)
    db_session.commit()

    # из документации устаревший вариант, наверное не стоит использовать
    # user = db_session.query(User).filter_by(login=login).first()
    assert user.id is not None, "Пользователь не был создан"


@pytest.mark.skipif
def test_duplicate_email(db_session: Session):
    '''Тестирование создания пользователя с дублирующимся email'''
    user_data = {
        'login': "UserName_1",
        'password': "User_Password_1",
        'email': "test_unique@mail.com"
    }
    new_user(user_data, db_session)

    login = "UserName_2"
    password = "User_Password_2"
    email = "test_unique@mail.com"

    with pytest.raises(ValueError, match=f'Пользователь с email {email} уже существует'):
        new_user(user_data, db_session)


@pytest.fixture
def test_account(db_session, test_create_user):
    user_id = 1
    name = 'New Account'
    currency = 'USD'
    symbol = '$'
    account = edit_account(db_session, user_id, name, currency, symbol)
    assert account.id, 'Счет не был создан'


@pytest.fixture
def test_transaction_create(transaction_data_create: dict, db_session: Session, test_account):
    transaction = Transaction(**transaction_data_create)
    db_session.add(transaction)
    db_session.commit()
    assert transaction.id, 'Транзакция не создана'


def test_transaction_update(db_session: Session, test_transaction_create):
    transaction = db_session.execute(select(Transaction)).first()[0]
    old_id = transaction.id
    old_comment = transaction.comment
    updated_transaction = update_transaction(transaction.id, {'comment': 'Updated'}, db_session)
    assert updated_transaction.id == old_id and old_comment != updated_transaction.comment
