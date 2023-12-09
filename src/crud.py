from sqlalchemy.orm import Session
from db import Session
from models import User, News


def create_user(login,password):
    with Session() as session:
        user = User(name=login,password=password)
        session.add(user)
        session.commit()

def user_list():
    with Session() as session:
        user_list = session.query(User).all() #Возврат __repr__
        return user_list

def last_news():
    with Session() as session:
        data = session.query(News).order_by(News.id.desc()).limit(10).all()
        return data

def create_news(title, text):
    with Session() as session:
        news = News(title=title, text=text)
        session.add(news)
        session.commit()

"""
# Способ прямого управления сессией. DANGER.
# Надо следить за session.close()
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

"""

if __name__=='__main__':
    user_list()
