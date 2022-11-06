from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'description', 'score']