from rest_framework import viewsets
from .serializers import OrderSerializer, OrderItemSerializer, PaymentSerializer
from .models import Order, OrderItem, Payment
# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('order_id')
    serializer_class = OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all().order_by('order_item_id')
    serializer_class = OrderItemSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all().order_by('payment_id')
    serializer_class = PaymentSerializer