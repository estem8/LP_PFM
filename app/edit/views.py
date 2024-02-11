from flask import Blueprint, render_template
from flask_login import current_user

from app.account.forms import AccountForm
from app.crud import fetch_accounts


edit = Blueprint('edit', __name__, url_prefix='/edit')


@edit.route('/', methods=['GET', 'POST'])
def test():
    form = AccountForm()
    accounts = fetch_accounts(current_user)
    return render_template('edit/edit.html', form=form, accounts=accounts)
