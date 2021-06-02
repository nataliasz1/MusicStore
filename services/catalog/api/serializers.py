from rest_framework import serializers

from .models import CatalogItem, Opinion, Category

class CatalogItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogItem
        fields = ('catalog_item_id', 'name', 'description', 'price', 'quantity', 'stars', 'category', 'slug')
       # fields = ('catalog_item_id')
        
 

class OpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opinion
        fields = ('opinion_id', 'product', 'user_id', 'text', 'stars')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "slug"]
