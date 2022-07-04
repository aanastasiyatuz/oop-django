from abstract.serializer import BaseSerializer

from models import Category, Product

class ProductSerializer(BaseSerializer):
    class Meta:
        fields = ["id","title", "price", "desc", "quantity", "category"]
        queryset = Product.objects

    def serialize_obj(self, obj):
        representation = super().serialize_obj(obj)
        representation['category'] = obj.category.title
        return representation

class CategorySerializer(BaseSerializer):
    class Meta:
        fields = ["title"]
        queryset = Category.objects