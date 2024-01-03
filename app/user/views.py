from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user

from app.user.forms import LoginForm, RegistrationForm


blueprint = Blueprint('user', __name__, url_prefix='/users')


@blueprint.route("/login")
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    title = "Вход"
    login_form = LoginForm()
    return render_template("user/login.html", page_title=title, form=login_form)


@blueprint.route("/signup")
def registration():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    title = "Регистрация"
    reg_form = RegistrationForm()
    return render_template("user/registration.html", page_title=title, form=reg_form)
