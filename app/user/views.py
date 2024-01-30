import flask_login

from flask import Blueprint, flash, redirect, render_template, request, url_for

from app import db
from app.common import UserAlreadyExistsError
from app.config import REMEMBER_COOKIE_DURATION
from app.crud import create_user
from app.models import User
from app.user.forms import LoginForm, RegistrationForm


blueprint = Blueprint('user', __name__, url_prefix='/users', template_folder='templates', static_folder='static')


@blueprint.route('/login')
def login():
    if flask_login.current_user.is_authenticated:
        return redirect(url_for('index'))
    title = 'Вход'
    login_form = LoginForm()
    return render_template('user/login.html', page_title=title, form=login_form)


@blueprint.route('/signup', methods=['GET', 'POST'], endpoint='signup')
def signup():
    if flask_login.current_user.is_authenticated:
        return redirect(url_for('lk.get_lk_page'))
    title = 'Регистрация'
    reg_form = RegistrationForm()
    if request.method == 'POST' and reg_form.validate():
        try:
            user = create_user(reg_form.data)
        except UserAlreadyExistsError:
            flash('Пользователь с таким именем или email уже существует')
            return render_template('user/signup.html', page_title=title, form=reg_form)
        flask_login.login_user(user)
        flash('Вы успешно зарегистрировались')
        return redirect(url_for('lk.get_lk_page'))
    return render_template('user/signup.html', page_title=title, form=reg_form)


@blueprint.route('/process-login', methods=['POST'])
def process_login():
    if flask_login.current_user.is_authenticated:
        return redirect(url_for('lk.get_lk_page'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.execute(db.select(User).filter_by(login=form.login.data)).scalar()
        if user and user.check_password(form.password.data):
            flask_login.login_user(user, remember=form.remember_me.data, duration=REMEMBER_COOKIE_DURATION)
            return redirect(url_for('lk.get_lk_page'))
    flash('Неверный логин или пароль')
    return redirect(url_for('user.login'))


@blueprint.route('/logout')
def logout():
    flask_login.logout_user()
    return redirect(url_for('index'))
