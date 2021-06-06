from rest_framework import serializers
from .models import Order, OrderItem, Payment

class OrderSerializer(serializers.ModelSerializer):
    order_items = serializers.StringRelatedField(read_only=True, many=True)
    payments = serializers.StringRelatedField(read_only=True, many=True)
    class Meta:
        model = Order
        #fields = '__all__'
        fields = ['order_id', 'status', 'total_amount', 'order_items', 'payments']

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'