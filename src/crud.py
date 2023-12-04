"""
manual
https://docs.sqlalchemy.org/en/13/orm/session_basics.html#session-basics
"""

from sqlalchemy.orm import Session
from db import engine
from models import User




"""
#create data in base
with Session(engine) as session:
    user = User(name='Test_user_2',password='test_password')
    session.add(user)
    session.commit()

    get_user = session.query(User).all()
    print(get_user)
"""


def create_user(login,password):
    session = Session(bind=engine) #Создали сессию
    try:
        new_user = User(login=login,password=password)
        session.add(new_user)
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close() #закрыли сессию

if __name__=='__main__':
    create_user('TestCrud','123pass')
