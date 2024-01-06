from flask_login import UserMixin
from sqlalchemy.orm import mapped_column, Mapped
from werkzeug.security import generate_password_hash, check_password_hash

from app.models import Base


# class User(Base, UserMixin):
#     """Пользователи
#     UserMixin нужен для работы flask_login. Добавляет в модель @property:
#     - is_active
#     - is_authenticated
#     - is_anonymous
#     и метод get_id"""
#
#     __tablename__ = "users"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     login: Mapped[str]
#     password: Mapped[str]
#     email: Mapped[str] = mapped_column(unique=True)
#
#     def __repr__(self):
#         return f'User login = {self.login}, email = {self.email}'
#
#     def set_password(self, password):
#         self.password = generate_password_hash(password)
#
#     def check_password(self, password):
#         return check_password_hash(self.password, password)
