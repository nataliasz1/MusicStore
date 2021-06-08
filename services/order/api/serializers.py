from rest_framework import serializers

from api.models import Order, OrderItem, Payment


class OrderItemSerializer(serializers.ModelSerializer):
    order_id = serializers.StringRelatedField(required=False)

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    payments = serializers.StringRelatedField(read_only=True, many=True)
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['order_id', 'status', 'total_amount', 'order_items', 'payments']
        depth = 1

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items')
        order = Order.objects.create(**validated_data)
        for item_data in order_items_data:
            OrderItem.objects.create(order_id=order, **item_data)
        return order


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
