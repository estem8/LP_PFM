from flask import Blueprint, current_app, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from sqlalchemy import select

from app import db
from app.common import UserAlreadyExistsError
from app.crud import create_user
from app.models import Account, User
from app.user.forms import LoginForm, RegistrationForm


blueprint = Blueprint('user', __name__, url_prefix='/users')


@blueprint.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    title = 'Вход'
    login_form = LoginForm()
    return render_template('user/login.html', page_title=title, form=login_form)


@blueprint.route('/signup', methods=['GET', 'POST'], endpoint='signup')
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('user.dashboard'))
    title = 'Регистрация'
    reg_form = RegistrationForm()
    if request.method == 'POST' and reg_form.validate():
        try:
            user = create_user(reg_form.data)
        except UserAlreadyExistsError:
            flash('Пользователь с таким именем или email уже существует')
            return render_template('user/signup.html', page_title=title, form=reg_form)
        login_user(user)
        flash('Вы успешно зарегистрировались')
        return redirect(url_for('user.dashboard'))
    return render_template('user/signup.html', page_title=title, form=reg_form)


@blueprint.route('/process-login', methods=['POST'])
def process_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.execute(db.select(User).filter_by(login=form.login.data)).scalar()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data, duration=current_app.config['REMEMBER_COOKIE_DURATION'])
            flash('Вы успешно авторизовались')
            return redirect(url_for('user.dashboard'))
    flash('Неверный логин или пароль')
    return redirect(url_for('user.login'))


@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@blueprint.route('/profile/')
@login_required
def profile():
    return f'Профиль {current_user.login}'


@blueprint.route('/dashboard')
@login_required
def dashboard():
    query = select(Account).where(Account.user_id == current_user.id)
    accounts = db.session.execute(query).scalars().all()
    return render_template('user/dashboard.html', accounts=accounts)
