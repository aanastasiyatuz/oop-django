from abstract.serializer import BaseSerializer

from models import Product

class ProductSerializer(BaseSerializer):
    class Meta:
        model = Product
        fields = ["id","title", "price", "desc", "quantity"]
        queryset = Product.objects
