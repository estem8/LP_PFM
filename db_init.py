from app.db import Base, engine


def db_init():
    """
    Создаем таблицы из метаданных Base - declarative_base
    Вызывается только один раз при пустой базе
    """
    from app.user.models import User
    from app.models import Account
    from app.transactions.models import Transaction
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    db_init()
