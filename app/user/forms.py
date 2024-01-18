from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length

MAX_LOGIN_LENGTH = 50
MIN_LOGIN_LENGTH = 4
MIN_PASSWORD_LENGTH = 6
MIN_EMAIL_LENGTH = 1
MAX_EMAIL_LENGTH = 50


class BaseLoginForm(FlaskForm):
    login = StringField(
        "Имя пользователя:",
        validators=[DataRequired(), Length(min=MIN_LOGIN_LENGTH, max=MAX_LOGIN_LENGTH)],
        render_kw={"class": "form-control"},
    )
    password = PasswordField(
        "Пароль:",
        validators=[DataRequired(), Length(min=MIN_PASSWORD_LENGTH)],
        render_kw={"class": "form-control"},
    )


class LoginForm(BaseLoginForm):

    submit = SubmitField("Войти", render_kw={"class": "btn btn-primary btn-lg"})
    remember_me = BooleanField(
        "Запомнить меня", default=True, render_kw={"class": "form-chek-input"})


class RegistrationForm(BaseLoginForm):
    email = StringField(
        "email:",
        validators=[DataRequired(), Length(min=MIN_EMAIL_LENGTH, max=MAX_EMAIL_LENGTH)],
        render_kw={"class": "form-control"},
    )
    confirm_password = PasswordField(
        'Повторите пароль: ',
        validators=[
            DataRequired(),
            EqualTo('password'),
        ],
        render_kw={'class': 'form-control'},
    )
    submit = SubmitField('Зарегистрироваться', render_kw={'class': 'btn btn-primary btn-lg'})
