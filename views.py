from serializers import ProductSerializer
from models import Product

def product_list():
    data = ProductSerializer().serialize_queryset()
    return data

def product_create():
    title = input("Введите название: ")
    price = input("Введите цену: ")
    desc = input("Введите описание: ")
    quantity = input("Введите кол-во")
    Product(title, price, desc, quantity)
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
