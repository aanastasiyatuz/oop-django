from serializers import ProductSerializer, CategorySerializer
from models import Category, Product

def product_list():
    data = ProductSerializer().serialize_queryset()
    return data

def product_create():
    title = input("Введите название: ")
    price = input("Введите цену: ")
    desc = input("Введите описание: ")
    quantity = input("Введите кол-во: ")
    print("Выберите категорию: ")
    for i, c in enumerate(Category.objects):
        print(f"{i}: {c.title}")
    category = Category.objects[int(input())]
    Product(title, price, desc, quantity, category)
    return "Продукт успешно создан"

def product_delete(p_id):
    Product.objects.pop(int(p_id))
    return "Продукт успешно удален"

def product_detail(p_id):
    product = Product.objects[int(p_id)]
    data = ProductSerializer().serialize_obj(product)
    return data

def product_update(p_id):
    product = Product.objects[int(p_id)]
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