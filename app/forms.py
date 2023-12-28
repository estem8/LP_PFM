from wtforms import Form, BooleanField, StringField, validators, SubmitField

class Account_Detail(Form):
    account_name = StringField('account name', [validators.Length(min=4, max=25)])
    currency = StringField('currency', [validators.Length(min=4, max=25)])
    symbol = StringField('symbol', [validators.Length(min=4, max=25)])
    submit = SubmitField('Submit')


class Transaction_Detail(Form):
    account_name = StringField('account name', [validators.Length(min=4, max=25)])
    type = StringField('transaction type i/o', [validators.Length(min=4, max=25)])
    amount = StringField('amount', [validators.Length(min=4, max=25)])
    comment = StringField('comment', [validators.Length(min=4, max=25)])
    submit = SubmitField('Submit')


class Account_Select(Form):
    select_account = StringField('select account', [validators.Length(min=4, max=25)])
    currency = StringField('currency', [validators.Length(min=4, max=25)])
    symbol = StringField('symbol', [validators.Length(min=4, max=25)])
    submit = SubmitField('Submit')