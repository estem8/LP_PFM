from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length


class LoginForm(FlaskForm):
    username = StringField(
        'Имя пользователя:',
        validators=[DataRequired(), Length(min=4, max=50)],
        render_kw={'class': 'form-control'},
    )
    password = PasswordField(
        'Пароль:',
        validators=[DataRequired(), Length(min=6)],
        render_kw={'class': 'form-control'},
    )
    remember_me = BooleanField('Запомнить меня', default=True, render_kw={'class': 'form-chek-input'})
    submit = SubmitField('Войти', render_kw={'class': 'btn btn-primary btn-lg'})


class RegistrationForm(FlaskForm):
    username = StringField(
        'Имя пользователя:',
        validators=[DataRequired(), Length(min=4, max=50)],
        render_kw={'class': 'form-control'},
    )
    password = PasswordField(
        'Пароль:',
        validators=[
            DataRequired(),
            Length(min=6, max=50),
        ],
        render_kw={'class': 'form-control'},
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
