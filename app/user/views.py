from flask import Blueprint, render_template
from app.user.forms import LoginForm, RegistrationForm


blueprint = Blueprint('user', __name__, url_prefix='/users')


@blueprint.route("/login")
def login():
    title = "Вход"
    login_form = LoginForm()
    return render_template("user/login.html", page_title=title, form=login_form)


@blueprint.route("/signup")
def registration():
    title = "Регистрация"
    reg_form = RegistrationForm()
    return render_template("user/registration.html", page_title=title, form=reg_form)
