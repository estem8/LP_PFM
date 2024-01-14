from datetime import date

import pytest


@pytest.fixture(
    scope='function',
    params=[
        {'account_id_from': 1, 'transaction_type': 'dept', 'amount': 150, 'date': date.today(), 'comment': 'test'},
        {'id': 1, 'account_id_from': 1, 'transaction_type': 'dept', 'amount': 300, 'date': date.today(),
         'comment': 'test'},
    ]
)
def transaction_data(request) -> dict:
    return request.param
