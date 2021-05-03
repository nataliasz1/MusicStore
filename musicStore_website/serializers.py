from rest_framework import serializers

from .models import CatalogItem, Opinion

class CatalogItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CatalogItem
        fields = ('catalog_item_id', 'name', 'description', 'price', 'quantity', 'stars')
 

class OpinionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Opinion
        fields = ('opinion_id', 'product', 'text', 'stars')



