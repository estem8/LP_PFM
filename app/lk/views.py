from flask import Blueprint, render_template
from flask_login import login_required


blueprint = Blueprint('lk', __name__, url_prefix='/lk', template_folder='templates', static_folder='static')


@login_required
@blueprint.get('/')
def get_lk_page():
    title = 'Личный кабинет'
    return render_template('lk/lk.html', page_title=title)
