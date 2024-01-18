from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user, logout_user

from app import Session
from app.crud import new_user
from app.user.forms import LoginForm, RegistrationForm
from app.models import User

blueprint = Blueprint('user', __name__, url_prefix='/users')


@blueprint.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    title = 'Вход'
    login_form = LoginForm()
    return render_template('user/login.html', page_title=title, form=login_form)


@blueprint.route("/signup", methods=["GET", "POST"], endpoint='signup')
def signup():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    title = "Регистрация"
    reg_form = RegistrationForm()
    if request.method == "POST" and reg_form.validate():
        new_user(reg_form.data)
        return redirect(url_for("index"))
    return render_template("user/signup.html", page_title=title, form=reg_form)


@blueprint.route('/process-login', methods=['POST'])
def process_login():
    form = LoginForm()
    if form.validate_on_submit():
        with Session() as session:
            user = session.query(User).filter_by(login=form.login.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('Вы успешно авторизовались')
            return redirect(url_for('index'))
    flash('Неверный логин или пароль')
    return redirect(url_for('user.login'))


@blueprint.route('/logout')
def logout():
    logout_user()
    flash('Вы успешно разлогинились')
    return redirect(url_for('index'))
