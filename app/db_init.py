from app.db import engine
from app.models import Base


def db_init():
    """
    Создаем таблицы из метаданных Base - declarative_base
    Вызывается только один раз при пустой базе
    """
    Base.metadata.create_all(engine)
    #Из документации при создании таблицы по умолчанию стоит параметр checkfirst=True
    #https://docs.sqlalchemy.org/en/20/core/metadata.html#sqlalchemy.schema.MetaData.create_all

if __name__ == "__main__":
    db_init()
