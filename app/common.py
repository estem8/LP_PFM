from enum import Enum


class DataBaseUniqError(Exception):
    pass


class DoesNotExistsError(Exception):
    pass


class UserAlreadyExistsError(Exception):
    pass


class TransactionsType(Enum):
    COSTS = '-'
    INCOME = '+'
    TRANSFER = '->'
