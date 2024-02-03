from flask import Blueprint, flash, redirect, url_for
from flask_login import login_required
from sqlalchemy.exc import DatabaseError

from app.crud import create_transaction
from app.transactions.forms import TransactionForm


blueprint = Blueprint('transactions', __name__, url_prefix='/transactions')


@login_required
@blueprint.post('/add')
def add():
    form = TransactionForm()
    if form.validate_on_submit():
        try:
            create_transaction(form.data)
        except DatabaseError:
            flash('Ошибка создания транзакции')
    else:
        flash('Невалидная форма')
    return redirect(url_for('user.dashboard'))


@login_required
@blueprint.route('/delete')
def delete():
    pass


@login_required
@blueprint.route('/patch')
def patch():
    pass
