from pprint import pprint

from shop.models import Category, Product
from urls import urlpatterns


cat = Category("phones")
Product("iphone", 345, "Iphone 10", 2, cat)
Product("samsung", 54, "Samsung...", 4, cat)
Product("lenovo", 12, "Lenovo...", 12, cat)

while True:
    try:
        url, arg = input("введите адрес: ").split("/")
    except ValueError:
        print("Enter a valid url")
        continue
    found = False
    for uri, view in urlpatterns:
        if url == uri.split("/")[0]:
            found = True
            try:
                if arg:
                    pprint(view(arg))
                else:
                    pprint(view())
            except Exception as e:
                print(e)
    if not found:
        print("404 Url Not found")