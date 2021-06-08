from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models import Order, OrderItem, Payment
from api.serializers import OrderItemSerializer, OrderSerializer, PaymentSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('order_id')
    serializer_class = OrderSerializer

    @action(methods=['get'], detail=False, url_path='user-id/(?P<user_id>[^/.]+)')
    def get_orders_per_user(self, request, user_id):
        user_orders = Order.objects.filter(user_id=user_id)
        if not user_orders:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = OrderSerializer(user_orders, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all().order_by('order_item_id')
    serializer_class = OrderItemSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all().order_by('payment_id')
    serializer_class = PaymentSerializer
