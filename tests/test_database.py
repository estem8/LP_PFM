import pytest

from app.common import UserAlreadyExistsError
from app.crud import creat_account, create_transaction, create_user, update_transaction


def test_create_user(user_data_create: dict) -> None:
    """Тест на запись в бд"""
    user = create_user(user_data_create)
    assert user.id is not None, 'Пользователь не был создан'


def test_duplicate_email(user_data_create_double: list[dict]) -> None:
    """Тестирование создания пользователя с дублирующимся email"""
    create_user(user_data_create_double[0])

    with pytest.raises(UserAlreadyExistsError):
        create_user(user_data_create_double[1])


def test_account(user_data_create: dict, account_data_create: dict) -> None:
    user = create_user(user_data_create)
    account_data_create['user_id'] = user.id
    account = creat_account(account_data_create)
    assert account.id, 'Счет не был создан'


def test_transaction_create(
    user_data_create: dict,
    account_data_create: dict,
    transaction_data_create: dict,
) -> None:
    user = create_user(user_data_create)
    account_data_create['user_id'] = user.id
    account = creat_account(account_data_create)
    transaction_data_create['account_id_from'] = account.id
    transaction = create_transaction(transaction_data_create)
    assert transaction.id, 'Транзакция не создана'


def test_transaction_update(
    user_data_create: dict,
    account_data_create: dict,
    transaction_data_create: dict,
) -> None:
    user = create_user(user_data_create)
    account_data_create['user_id'] = user.id
    account = creat_account(account_data_create)
    transaction_data_create['account_id_from'] = account.id
    transaction = create_transaction(transaction_data_create)
    old_id = transaction.id
    old_comment = transaction.comment
    updated_transaction = update_transaction(transaction.id, {'comment': 'Updated'})
    assert updated_transaction.id == old_id and old_comment != updated_transaction.comment
