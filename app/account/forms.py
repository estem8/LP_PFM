from wtforms import validators
from wtforms.fields.simple import StringField, SubmitField
from wtforms.form import Form


class AccountForm(Form):
    name = StringField('account name', [validators.Length(min=1, max=25)])
    currency = StringField('currency', [validators.Length(min=1, max=25)])
    symbol = StringField('symbol', [validators.Length(min=1, max=25)])
    submit = SubmitField('Submit')
