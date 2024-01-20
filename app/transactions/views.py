from flask import Blueprint, flash, render_template
from flask_login import login_required
from sqlalchemy.exc import DatabaseError

from app.crud import create_transaction
from app.transactions.forms import TransactionForm

blueprint = Blueprint(
    'transactions', __name__, url_prefix='/transactions', template_folder='templates', static_folder='static'
)


# @login_required
@blueprint.route('/add', methods=['GET', 'POST'])
def add():
    page_title = 'Добавление Транзакции'
    form = TransactionForm()
    if form.validate_on_submit():
        try:
            create_transaction(form.data)
        except DatabaseError:
            flash('Ошибка создания транзакции')
    else:
        flash('Невалидная форма')
    return render_template('transactions/add.html', page_title=page_title, form=form)


@login_required
@blueprint.route('/delete')
def delete():
    pass


@login_required
@blueprint.route('/patch')
def patch():
    pass
