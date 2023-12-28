from psycopg2 import OperationalError
from sqlalchemy.orm.session import Session
from app.config import DB_URL
import pytest
from sqlalchemy import Engine, create_engine, select
from sqlalchemy.orm import sessionmaker
from app.models import *
from app.crud import create_user

@pytest.fixture()
def engine():
    # Пока нету .env или в память как сейчас sqlite или PostgresSQL и очистка Base.metadata.drop_all(engine)
    # engine = create_engine('postgresql://user:password@localhost:5432/db', echo=True)
    engine = create_engine('sqlite:///', echo=True)
    Base.metadata.create_all(engine)
    try:
        yield engine
    finally:
        pass
        # Base.metadata.drop_all(engine)

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
        pytest.fail(f"Failed to connect to the database: {e}")


def test_create_user(db_session: Session):
    '''Тест на запись в бд'''
    login = "testuser1"
    password = "testpassword1"
    email = "test@mail1"

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
    login = "testuser2"
    password = "testpassword2"
    email = "test@mail2"
    create_user(db_session, login, password, email)

    login = "testuser3"
    password = "testpassword4"
    email = "test@mail2"
    with pytest.raises(ValueError, match=f'Пользователь с email {email} уже существует'):
        create_user(db_session, login, password, email)