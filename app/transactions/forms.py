from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators
from wtforms.fields.choices import SelectField
from wtforms.fields.datetime import DateField
from wtforms.fields.numeric import FloatField
from wtforms.validators import DataRequired, ValidationError

from app.common import TransactionsType
from app.crud import fetch_account


def validate_field_by_list_values(value_list: list[str], message='Некорректное значение поля'):
    def _validate(form, field):
        if field.data not in value_list:
            raise ValidationError(message)

    return _validate


def validate_account_exists_by_account_id(form, field):
    if field.data is None:
        return
    instance = fetch_account(account_id=field.data)
    if not instance:
        raise ValidationError('Не найден счет у текущего пользователя')


class TransactionForm(FlaskForm):
    account_id = SelectField('Счет', render_kw={'class': 'form-control'}, coerce=int)
    transaction_type = SelectField(
        'Тип операции',
        [DataRequired()],
        choices=[(tr.value, tr.name) for tr in TransactionsType],
        render_kw={'class': 'form-control hidden'},
    )
    amount = FloatField('Сумма', [DataRequired()], render_kw={'class': 'form-control'})
    date = DateField('Дата операции', [DataRequired()], render_kw={'class': 'form-control'})
    comment = StringField('Комментарий', [validators.Length(max=255)], render_kw={'class': 'form-control'})
    submit = SubmitField('Сохранить', render_kw={'class': 'btn btn-primary btn-lg'})
