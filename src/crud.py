from sqlalchemy.orm import Session
from db import engine, Session
from models import User


def create_user(login,password):
    with Session() as session:
        user = User(name=login,password=password)
        session.add(user)
        session.commit()

        get_user = session.query(User).all()
        print(get_user)



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