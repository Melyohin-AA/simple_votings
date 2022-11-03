import datetime

from django.contrib.auth.models import User
from main.models import UserData, VoteFact
from exceptions import Exceptions


class DB_UserTools:
    @staticmethod
    def try_register_user(login, password, name, test) -> (bool, str):
        if not (isinstance(login, str) and isinstance(password, str) and
                isinstance(name, str) and isinstance(test, bool)):
            Exceptions.throw(Exceptions.argument_type)
        if not ((0 < len(login) <= 64) and (0 < len(name) <= 64) and (0 < len(password) <= 64)):
            return False, "Не должно быть пустых полей!"
        if len(User.objects.filter(username=login)) > 0:
            return False, "Пользователь с данным логином уже существует!"
        if login == "$_del":
            return False, "Логин не может быть '$_del'!"
        user = User(first_name=name, username=login, date_joined=datetime.datetime.today())
        user.set_password(password)
        user.save()
        user_data = UserData(user=user, test=test)
        user_data.save()
        return True, None

    @staticmethod
    def try_get_user_data(user) -> (UserData, str):
        if not isinstance(user, User):
            Exceptions.throw(Exceptions.argument_type)
        user_data = UserData.objects.filter(user=user)
        if len(user_data) != 1:
            return None, "Некорректная конфигурация пользовательских данных!"
        return user_data[0], None

    @staticmethod
    def try_find_user(login) -> (User, str):
        if not isinstance(login, str):
            Exceptions.throw(Exceptions.argument_type)
        user = DB_UserTools.find_user(login)
        if user is None:
            return None, "Пользователь не найден!"
        return user, None

    @staticmethod
    def find_user(login) -> User:
        user = User.objects.filter(username=login)
        if len(user) == 0:
            return None
        return user[0]

    @staticmethod
    def try_find_user_with_id(id) -> (User, str):
        user = User.objects.filter(id=id)
        if len(user) == 0:
            return None, "Пользователь не найден!"
        return user[0], None

    @staticmethod
    def check_user_activation_required(user) -> (bool, str):
        if not isinstance(user, User):
            Exceptions.throw(Exceptions.argument_type)
        user_data = UserData.objects.filter(user=user)
        if len(user_data) != 1:
            return False, "Некорректная конфигурация пользовательских данных!"
        if not user_data[0].activated:
            return False, "Пользователь не активирован!"
        return True, None

    @staticmethod
    def can_vote(user, voting) -> bool:
        running = not voting.completed and voting.started
        if not running:
            return False
        ok, _ = DB_UserTools.check_user_activation_required(user)
        if not ok:
            return False
        vars = VoteFact.objects.filter(user=user, voting=voting)
        return len(vars) == 0

    @staticmethod
    def clear_user_list():
        UserData.objects.all().delete()
        User.objects.all().delete()
