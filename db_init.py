from app.db import engine
from app.models import Base

def db_init():
    """
    Создаем таблицы из метаданных Base - declarative_base
    Вызывается только один раз при пустой базе
    """
    Base.metadata.create_all(engine)
    #Я проверил по документации create_all перед созданием делает проверку на exists
    #так что мне кажется эту функцию можно пихать в app/__init__.py на каждый запуск

if __name__ == "__main__":
    db_init()
