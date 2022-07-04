from abstract.utils import get_obj_or_404
from account.models import User

from .serializers import CommentSerializer, ProductSerializer, CategorySerializer
from .models import Category, Comment, Product


def product_list():
    data = ProductSerializer().serialize_queryset()
    return data

def product_create():
    title = input("Введите название: ")
    price = input("Введите цену: ")
    desc = input("Введите описание: ")
    quantity = input("Введите кол-во: ")
    print("Выберите категорию: ")
    for c in Category.objects:
        print(c.title)
    category = get_obj_or_404(Category, "title", input())
    Product(title, price, desc, quantity, category)
    return "Продукт успешно создан"

def product_delete(p_id):
    product = get_obj_or_404(Product, "id", int(p_id))
    Product.objects.remove(product)
    return "Продукт успешно удален"

def product_detail(p_id):
    product = get_obj_or_404(Product, "id", int(p_id))
    data = ProductSerializer().serialize_obj(product)
    return data

def product_update(p_id):
    product = get_obj_or_404(Product, "id", int(p_id))
    field = input("Введите поле для изменения: ")
    if field in dir(product):
        value = input(f"{field} = ")
        type_ = type(product.__getattribute__(field))
        product.__setattr__(field, type_(value))
    return product_detail(p_id)

def category_list():
    data = CategorySerializer().serialize_queryset()
    return data

def create_category():
    title = input("Введите название: ")
    Category(title)
    return "Категория была успешно создана"

def create_comment(email):
    user = get_obj_or_404(User, "email", email)
    print("Выберите продукт: ")
    for p in Product.objects:
        print(p.title)
    title = input()
    product = get_obj_or_404(Product, "title", title)
    body = input("Введите комментарий: ")
    Comment(user, product, body)
    return "Комментарий успешно добавлен"

def comments_list():
    data = CommentSerializer().serialize_queryset()
    return data