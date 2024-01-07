from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length


class LoginForm(FlaskForm):
    username = StringField(
        "Имя пользователя:",
        validators=[DataRequired(), Length(min=4, max=50)],
        render_kw={"class": "form-control"},
    )
    password = PasswordField(
        "Пароль:",
        validators=[DataRequired(), Length(min=6)],
        render_kw={"class": "form-control"},
    )
    submit = SubmitField("Войти", render_kw={"class": "btn btn-primary btn-lg"})
    remember_me = BooleanField(
        "Запомнить меня", default=True, render_kw={"class": "form-chek-input"}
    )


class RegistrationForm(FlaskForm):
    username = StringField(
        "Имя пользователя:",
        validators=[Length(min=4, max=50)],  # TODO: required
        render_kw={"class": "form-control"},
    )
    password = PasswordField(
        "Пароль:",
        validators=[
            DataRequired(),
            Length(min=6, max=50),
        ],
        render_kw={"class": "form-control"},
    )
    confirm_password = PasswordField(
        "Повторите пароль: ",
        validators=[
            DataRequired(),
            EqualTo("password"),
        ],
        render_kw={"class": "form-control"},
    )
    submit = SubmitField(
        "Зарегистрироваться", render_kw={"class": "btn btn-primary btn-lg"}
    )
