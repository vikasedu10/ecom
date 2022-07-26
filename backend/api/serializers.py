from rest_framework import serializers
from frontend.models import Product, Cart

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = ('name', 'category', 'tags', 'description', 'product_image', 'price')
        fields = "__all__"

