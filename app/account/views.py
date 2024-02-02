import flask_login

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user

from app.account.forms import AccountForm
from app.crud import create_account, fetch_account

blueprint = Blueprint('account', __name__, url_prefix='/account')


@flask_login.login_required
@blueprint.get('/')
def get_create_page():
    form = AccountForm()
    return render_template('edit/edit.html', form=form)


@flask_login.login_required
@blueprint.route('/account', methods=['GET', 'POST'])
def account_create():
    account_form = AccountForm(request.form)
    if not account_form.validate():
        flash('Invalid input.')
        return redirect(url_for('account.get_create_page'))
    account_exists = fetch_account(account_form.name.data, account_form.currency.data, current_user)
    if account_exists.id:
        flash('The account already exists')
    else:
        create_account(
            name=account_form.name.data,
            user_id=current_user.id,
            currency=account_form.currency.data,
            symbol=account_form.symbol.data,
        )
        flash('The account has been successfully added')
    return redirect(url_for('account.get_create_page'))
