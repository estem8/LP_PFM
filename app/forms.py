from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo


class LoginForm(FlaskForm):
    username = StringField(
        "Имя пользователя:",
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )
    password = PasswordField(
        "Пароль:",
        validators=[
            DataRequired(),
            Length(min=6, message="Пароль должен быть не менее %(min) символов"),
        ],
        render_kw={"class": "form-control"},
    )
    submit = SubmitField("Войти", render_kw={"class": "btn btn-primary btn-lg"})


class RegistrationForm(FlaskForm):
    username = StringField(
        "Имя пользователя: ",
        validators=[
            Length(min=4, max=50, message="Имя должно быть от 4 до 50 символов")
        ],
        render_kw={"class": "form-control"},
    )
    password = PasswordField(
        "Пароль: ",
        validators=[
            DataRequired(),
            Length(min=6, max=50, message=f"Пароль должен быть от 6 до 50 символов"),
        ],
        render_kw={"class": "form-control"},
    )
    confirm_password = PasswordField(
        "Повторите пароль: ",
        validators=[DataRequired(), EqualTo("password", message="Пароли не совпадают")],
        render_kw={"class": "form-control"},
    )
    submit = SubmitField("Регистрация", render_kw={"class": "btn btn-primary btn-lg"})
