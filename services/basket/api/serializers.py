from rest_framework import serializers

from .models import BasketItem, BasketSession

class BasketItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketItem
        fields = ('basket_item_id', 'basket_session_id','catalog_item_id', 'slug', 'quantity')


class BasketSessionSerializer(serializers.HyperlinkedModelSerializer):
    basket_item = BasketItemSerializer(many=True)
    class Meta:
        model = BasketSession
        fields = ('basket_id', 'user_id', 'basket_item')
        depth = 1

    def create(self, validated_data):
        basket_items_data = validated_data.pop('basket_item')
        basket_session = BasketSession.objects.create(**validated_data)
        for basket_data in basket_items_data:
            BasketItem.objects.create(basket_session_id=basket_session, **basket_data)
        return basket_session

