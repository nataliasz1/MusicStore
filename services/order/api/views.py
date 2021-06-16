from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models import Order, OrderItem, Payment
from api.serializers import OrderItemSerializer, OrderSerializer, PaymentSerializer
from rest_framework.decorators import api_view
import requests

import uuid 


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

@api_view(http_method_names=["GET"])
def create_order(request):
    user_id = request.query_params.get("user_id")
    if user_id == None:
        user_id = uuid.uuid4()

    response = requests.get("http://basket-web:8004/basket/createOrder/?user_id=%d" % int(user_id)).json()
  #  response = requests.get("http://127.0.0.1:8002/basket/createOrder/?user_id=%d" % int(user_id)).json()
    queryBefore= Order.objects.all().count()
    order = Order()
    order.user_id = user_id
    order.total_amount = 0
    order.save()
    queryset = Order.objects.filter(user_id=user_id).order_by('-order_id')

    order_serializer = OrderSerializer(queryset, many=True) 

    for i in range (0, len(response)):
        order_item = OrderItem()
        order_item.order_id = Order.objects.filter(order_id=order_serializer.data[0]['order_id']).first()
        order_item.catalog_item_id = response[i]['catalog_item_id']
            
        order_item.quantity = response[i]["quantity"]
        order_item.price = requests.get("http://catalog-web:8002/product/basket/?prod_id=%d" % order_item.catalog_item_id).json()[0]['price']
      #  order_item.price = requests.get("http://127.0.0.1:8003/product/basket/?prod_id=%d" % order_item.catalog_item_id).json()[0]['price']
        order_item.save()
        order = Order.objects.filter(order_id=order_serializer.data[0]['order_id'])
        order.update(total_amount=order_item.price+order_item.price)
        order.first().save()

    queryAfter= Order.objects.all().count()

    if (queryAfter == queryBefore+1):
        return Response({'success': True} , status=200)
    else : return Response({'success': False} , status=200)

""" 
    if queryset.count() == 0:
        return Response( status = 404)
    else :
        return Response( basket_session_serializer.data, status = 200)
 """