from db import Session
from faker import Faker
from models import User, News
fake = Faker()



def generate_user(num):
    profiles = []
    for _ in range(num):
        profile = fake.simple_profile()  
        profile['password'] = fake.password(length=12)
        profiles.append(profile)
    return profiles


def generate_post():
    post = fake.sentence(nb_words=50)
    return post

def create_news(num):
    with Session() as session:
        for _ in range(num):
            news = News(
                title = fake.sentence(nb_words=5),
                text = fake.sentence(nb_words=50),
                date = fake.date()
            )
            session.add(news)
            session.commit()

def create_user_in_db(num):
    with Session() as session:
        for _ in generate_user(num):
            users = User(
                first_name=_['name'],
                login=_['username'],
                password=_['password'],
                email=_['mail'],
            )
            session.add(users)
            session.commit()
        
        
if __name__=='__main__':
    create_user_in_db(10)
    create_news(10)