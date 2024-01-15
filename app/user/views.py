from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user, login_user, logout_user
from app import Session
from app.user.forms import LoginForm, RegistrationForm
from app.user.models import User
from app.crud import new_user
blueprint = Blueprint('user', __name__, url_prefix='/users')


@blueprint.route("/login")
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    title = "Вход"
    login_form = LoginForm()
    return render_template("user/login.html", page_title=title, form=login_form)


@blueprint.route("/signup", methods=["POST", "GET"], endpoint='registration')
def registration():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    title = "Регистрация"
    reg_form = RegistrationForm()
    if request.method == "POST" and reg_form.validate():
        new_user(reg_form.data)
    return render_template("user/registration.html", page_title=title, form=reg_form)


@blueprint.route('/process-login', methods=['GET', 'POST'])
def process_login():
    form = LoginForm()
    if form.validate_on_submit():
        with Session() as session:
            user = session.query(User).filter_by(login=form.username.data).first()
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
