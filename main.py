from models import Product
from urls import urlpatterns

Product("iphone", 345, "Iphone 10", 2)
Product("samsung", 54, "Samsung...", 4)
Product("lenovo", 12, "Lenovo...", 12)

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
            if arg:
                print(view(arg))
            else:
                print(view())
    if not found:
        print("404 Not found")