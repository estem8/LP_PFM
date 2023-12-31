from flask import Blueprint, render_template
from app.edit.forms import AccountDetail

edit = Blueprint('edit', __name__, template_folder='templates', static_folder='static')
@edit.route("/", methods=["GET", "POST"])
def test():
    form = AccountDetail()
    return render_template('edit/edit.html', form=form)