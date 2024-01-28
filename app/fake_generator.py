"""
Генератор Fake данных
"""

import matplotlib.pyplot as plt

from faker import Faker

from app.crud import create_user


fake = Faker()


def generate_user(num):
    profiles = []
    for _ in range(num):
        profile = fake.simple_profile()
        profile['password'] = fake.password(length=12)
        profiles.append(profile)
    return profiles


def create_user_in_db(num):
    for profile in generate_user(num):
        create_user(
            {
                'first_name': profile['name'],
                'login': profile['username'],
                'password': profile['password'],
                'email': profile['mail'],
            }
        )


my_list = [
    'Яблоки',
    'Бананы',
    'Апельсины',
    'Молоко',
    'Хлеб',
    'Яйца',
    'Курица',
    'Рис',
    'Паста',
    'Помидоры',
    'Шпинат',
    'Морковь',
    'Картошка',
    'Сыр',
    'Йогурт',
    'Лосось',
    'Фарш говяжий',
    'Оливковое масло',
    'Кофе',
    'Чай',
    'Сахар',
    'Мука',
    'Масло',
    'Мед',
    'Арахисовое масло',
    'Варенье',
    'Хлопья',
    'Лук',
    'Чеснок',
    'Болгарский перец',
    'Авокадо',
    'Салат',
    'Огурцы',
    'Брокколи',
    'Голубика',
    'Клубника',
    'Виноград',
    'Чипсы',
    'Газировка',
    'Вода',
]


"""
SELECT product_name, COUNT(*) as product_count
FROM outcome
GROUP BY product_name
ORDER BY product_count DESC
LIMIT 10
^^^^^^
RAW SQL
"""
quant = []
label = []


def generate_image():
    plt.pie(quant, labels=label, autopct='%1.1f%%')
    plt.show()


if __name__ == '__main__':
    # create_user_in_db(10) #Тут создаем 10 пользователей
    # generate_outcome_2(50) # Проходимся по каждому пользователю и добавляем 50 записей в таблицу покупок
    # create_news(10) #10 записей в таблицу новости
    # most_popular()
    generate_image()
