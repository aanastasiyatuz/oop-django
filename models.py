import permissions

class Category:
    objects = []

    def __init__(self, title):
        self.title = title
        Category.objects.append(self)
    
    def __str__(self):
        return self.title

class Product:
    objects = []
    _id = 0

    def __init__(self, title, price, description, quantity, category):
        self.id = Product._id
        self.title = title
        self.price = price
        self.desc = description
        self.quantity = quantity
        self.category = category
        Product.objects.append(self)
        Product._id += 1

    def __str__(self):
        return f"{self.title} [{self.quantity}] - ${self.price}\n({self.desc[:20]})"

class Comment:
    objects = []

    def __init__(self, user, product, body):
        permissions.login_required(user)
        from datetime import datetime
        self.user = user
        self.product = product
        self.body = body
        self.created_at = datetime.now()
        Comment.objects.append(self)
    
    def __str__(self):
        return f"{self.user.email} - [{self.created_at}] - {self.body}"

class User:
    objects = []

    def __init__(self, email, name, sex):
        self.email = email
        self.name = name
        self.sex = sex
        self.__password = None
        self.is_authenticated = False
        print(f"успешно создан юзер {self.email}")
        User.objects.append(self)

    def register(self, password, password_confirm):
        if password != password_confirm:
            raise Exception("Пароли не совпадают")
        self.__password = password
        print(f"успешно зарегистрирован юзер {self.email}")

    def login(self, password):
        if self.__password != password:
            raise Exception("Пароль не верный")
        self.is_authenticated = True
        print(f"успешно залогинился юзер {self.email}")

    def logout(self):
        permissions.login_required(self)
        self.is_authenticated = False
        print(f"успешно вышел юзер {self.email}")

    def __str__(self):
        return self.email


