from rest_framework import serializers

from .models import CatalogItem, Opinion, Category

class CatalogItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogItem
        fields = ('id', 'name', 'description', 'price', 'quantity', 'stars', 'category', 'slug')
 

class OpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opinion
        fields = ('id', 'product', 'text', 'stars')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "slug"]
