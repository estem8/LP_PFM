"""
Генератор Fake данных
"""
from random import randrange
from db import Session
from faker import Faker
from models import User, News, Outcome, Income
fake = Faker()


def generate_user(num):
    profiles = []
    for _ in range(num):
        profile = fake.simple_profile()  
        profile['password'] = fake.password(length=12)
        profiles.append(profile)
    return profiles

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


my_list = ["Яблоки", "Бананы", "Апельсины", "Молоко", "Хлеб", "Яйца", "Курица", "Рис", "Паста", "Помидоры", "Шпинат", "Морковь", "Картошка", "Сыр", "Йогурт", "Лосось", "Фарш говяжий", "Оливковое масло", "Кофе", "Чай", "Сахар", "Мука", "Масло", "Мед", "Арахисовое масло", "Варенье", "Хлопья", "Лук", "Чеснок", "Болгарский перец", "Авокадо", "Салат", "Огурцы", "Брокколи", "Голубика", "Клубника", "Виноград", "Чипсы", "Газировка", "Вода"]


def generate_outcome_2(num):
    with Session() as session:
        users = session.query(User).all()
        user_ids = [user.id for user in users]
        for id in user_ids:
            for _ in range(num):
                out = Outcome(
                    user_id = id,
                    product_name = fake.word(ext_word_list=my_list),
                    quantity = fake.random_int(1,10),
                    price = randrange(1000),
                    purchase_date = fake.date_this_month(),
                )
                session.add(out)
                session.commit()


if __name__=='__main__':
    create_user_in_db(10) #Тут создаем 10 пользователей
    generate_outcome_2(50) # Проходимся по каждому пользователю и добавляем 50 записей в таблицу покупок
    create_news(10) #10 записей в таблицу новости   
    