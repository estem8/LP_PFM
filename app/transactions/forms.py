import datetime

# from sqlalchemy import and_
from wtforms import Form, StringField, SubmitField, validators
from wtforms.fields.datetime import DateField
from wtforms.fields.numeric import FloatField, IntegerField
from wtforms.validators import DataRequired, ValidationError

from app.config import OPER_TYPE_CARD_DEPT

# from app.db import Base, Session
# from app.models import Account

# from app.user.models import User

OPER_TYPE_LIST = [
    OPER_TYPE_CARD_DEPT,
]


def validate_field_by_list_values(value_list: list[str], message='Некорректное значение поля'):
    def _validate(form, field):
        if field.data not in value_list:
            raise ValidationError(message)

    return _validate


def validate_account_exists(form, field):
    # current_user from flask_login
    # if field.data is not None:
    #     with Session() as session:
    #         instance = session.query(Account).filter_by(and_(user=current_user, id=field.data).first())
    #         if not instance:
    #             raise ValidationError('Не найден счет у текущего пользователя')
    pass


# def validate_amount(form, amount):
#     if form.type == OPER_TYPE_CARD_DEPT:
#         current_balance = get_current_amount(form.account_id_from.data)  TODO реализовать get_current_amount
#         if current_amount < amount.data:
#             raise ValidationError('Недостаточно средств для данной операции')


def validate_date(form, field):
    try:
        datetime.date.fromisoformat(field.data)
    except Exception:
        raise ValidationError('Недопустимая дата или некорректный формат')


class TransactionForm(Form):
    account_id_from = IntegerField(
        # TODO передавать в форму на фронт список счетов юзверя и брать из формы id account
        'Счет',
        [validate_account_exists],
        render_kw={'class': 'form-control'},
    )
    account_id_to = IntegerField('Счет', [validate_account_exists], render_kw={'class': 'form-control'})
    transaction_type = StringField(
        'Тип операции',
        [DataRequired(), validate_field_by_list_values(OPER_TYPE_LIST)],
        render_kw={'class': 'form-control'},
    )
    amount = FloatField('Сумма', [DataRequired()], render_kw={'class': 'form-control'})
    # 'amount', [DataRequired(), validate_amount], render_kw={'class': 'form-control'})  TODO допилить проверку баланса
    date = DateField('Дата операции', [DataRequired(), validate_date], render_kw={'class': 'form-control'})
    comment = StringField('Комментарий', [validators.Length(max=255)], render_kw={'class': 'form-control'})
    submit = SubmitField('Сохранить', render_kw={'class': 'btn btn-primary btn-lg'})
