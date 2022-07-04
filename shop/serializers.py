from abstract.serializer import BaseSerializer

from .models import Category, Comment, Product


class ProductSerializer(BaseSerializer):
    class Meta:
        fields = ["id","title", "price", "desc", "quantity", "category"]
        queryset = Product.objects

    def serialize_obj(self, obj):
        representation = super().serialize_obj(obj)
        representation['category'] = obj.category.title
        representation['comments'] = CommentSerializer().serialize_queryset(obj.comments)
        return representation

class CategorySerializer(BaseSerializer):
    class Meta:
        fields = ["title"]
        queryset = Category.objects

class CommentSerializer(BaseSerializer):
    class Meta:
        fields = ["body", "created_at"]
        queryset = Comment.objects
    
    def serialize_obj(self, obj):
        representation = super().serialize_obj(obj)
        representation["user"] = obj.user.email
        representation["product"] = obj.product.title
        return representation