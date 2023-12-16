from types import NoneType
from db import Session
from models import User, News, Income, Outcome
from sqlalchemy import select

def test():
    login='afritz'
    password='K5L%edTPeEpP'
    with Session() as session:
        user = select(User).where(User.login==login, User.password == password)
        print(i.__dict__ for i in session.execute(user))
        # result = session.execute(user)
        # if result():
        #     print('OK')
if __name__=='__main__':
    test()