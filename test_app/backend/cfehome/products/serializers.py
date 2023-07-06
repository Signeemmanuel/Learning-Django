from rest_framework import serializers
from .models import Product
from api.validators import unique_product_title
from api.serializers import UserPublicSerializer

class ProductSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    my_discount = serializers.SerializerMethodField(read_only=True)
    title = serializers.CharField(validators=[unique_product_title])
    # edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.EmailField(read_only=True)
    body = serializers.CharField(source='content')
    class Meta:
        model = Product
        fields = [
            'url',
            # 'edit_url',
            "user",
            "pk",
            "title",
            "body",
            "price",
            "sale_price",
            "my_discount",
            "public",
            "path",
        ]
        
    # def get_edit_url (self, obj):
    #     return "http://localhost:8000/api/products/" + str(obj.pk) + '/'

    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
    