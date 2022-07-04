import permissions

class User:
    objects = []

    def __init__(self, email, name, sex):
        self.email = email
        self.name = name
        self.sex = sex
        self.__password = None
        self.is_authenticated = False
        User.objects.append(self)

    def register(self, password, password_confirm):
        if password != password_confirm:
            raise Exception("Пароли не совпадают")
        self.__password = password

    def login(self, password):
        if self.__password != password:
            raise Exception("Пароль не верный")
        self.is_authenticated = True

    def logout(self):
        permissions.login_required(self)
        self.is_authenticated = False

    def __str__(self):
        return self.email
