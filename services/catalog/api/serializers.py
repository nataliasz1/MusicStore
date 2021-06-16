from rest_framework import serializers

from .fibase_config import storage
from .models import CatalogItem, Opinion, Category, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    img_url = serializers.SerializerMethodField()

    class Meta:
        model = ProductImage
        fields = ('image_id', 'catalog_item_id', 'added', 'img_url')

    def get_img_url(self, obj):
        return storage.child(obj.file).get_url('')


class CatalogItemSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True)

    class Meta:
        model = CatalogItem
        fields = (
            'catalog_item_id', 'name', 'description', 'description_long', 'price', 'quantity', 'stars', 'category',
            'slug',
            'images')


class OpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opinion
        fields = ('opinion_id', 'product', 'user_id', 'text', 'stars')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']
