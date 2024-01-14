from flask import Blueprint, flash, render_template, request
from flask_login import login_required

from app.crud import new_transaction
from app.transactions.forms import TransactionForm

blueprint = Blueprint(
    'transactions', __name__, url_prefix='/transactions', template_folder='templates', static_folder='static'
)


# @login_required
@blueprint.route('/add', methods=['GET', 'POST'])
def add():
    page_title = 'Добавление Транзакции'
    form = TransactionForm()
    if request.method == 'GET':
        return render_template('transactions/add.html', page_title=page_title, form=form)
    if not form.validate():
        flash('Невалидная форма')
        return render_template('transactions/add.html', form=form)
    transaction = new_transaction(form.data)
    if not transaction.id:
        raise Exception('не удалось записать в БД')
    return


@login_required
@blueprint.route('/delete')
def delete():
    pass


@login_required
@blueprint.route('/patch')
def patch():
    pass
