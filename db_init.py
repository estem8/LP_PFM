from app.db import engine
from app.models import Base


def db_init():
    """
    Создаем таблицы из метаданных Base - declarative_base
    Вызывается только один раз при пустой базе
    """
    from app.models import Account, Transaction, User
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    db_init()
