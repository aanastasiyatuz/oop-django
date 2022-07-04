from abstract.utils import get_obj_or_404

from .models import User
from .serializers import UserSerializer


def users_list():
    data = UserSerializer().serialize_queryset()
    return data

def register():
    email = input("Введите email: ")
    name = input("Введите имя: ")
    sex = input("Введите пол (ж/м): ")
    user = User(email, name, sex)
    password = input("Введите пароль: ")
    user.register(password, password)
    return "Юзер успешно зарегистрирован"

def login(email):
    user = get_obj_or_404(User, "email", email)
    password = input("Введите пароль: ")
    user.login(password)
    return "Вы успешно зарегистрировались"

def logout(email):
    user = get_obj_or_404(User, "email", email)
    user.logout()
    return "Вы успешно вышли"

def user_profile(email):
    user = get_obj_or_404(User, "email", email)
    data = UserSerializer().serialize_obj(user)
    return data
