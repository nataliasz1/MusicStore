from rest_framework import serializers

from .models import BasketItem, BasketSession


class BasketSessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
   
        model = BasketSession
        fields = ('basket_id','user_id')



class BasketItemSerializer(serializers.ModelSerializer):
    class Meta:
   
        model = BasketItem
        fields = ('basket_item_id', 'basket_session_id', 'catalog_item_id', 'quantity')




      