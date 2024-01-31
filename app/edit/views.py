from flask import Blueprint, render_template, request

from app.database import db
from app.edit.forms import AccountDetail
from app.models import Account


edit = Blueprint('edit', __name__, url_prefix='/edit')


@edit.route('/', methods=['GET', 'POST'])
def test():
    form = AccountDetail()
    return render_template('edit/edit.html', form=form)


@edit.route('/account', methods=['GET', 'POST'])
def account_editor():
    account_form = AccountDetail(request.form)
    if request.method == 'POST' and account_form.validate():
        add_account = Account(
            user_id=1,
            name=account_form.account_name.data,
            currency=account_form.currency.data,
            symbol=account_form.symbol.data,
        )
        db.session.add(add_account)
        db.session.commit()
    return render_template('edit/account.html', form=account_form)
