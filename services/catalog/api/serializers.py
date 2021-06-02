from rest_framework import serializers

from .models import CatalogItem, Opinion, Category, ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"


class CatalogItemSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True)
    class Meta:
        model = CatalogItem
        fields = ('catalog_item_id', 'name', 'description', 'price', 'quantity', 'stars', 'category', 'slug', 'images')
       
        
 

class OpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opinion
        fields = ('opinion_id', 'product', 'user_id', 'text', 'stars')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "slug"]
