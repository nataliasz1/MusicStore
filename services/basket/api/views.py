from django.http import HttpResponse
from rest_framework import views, viewsets, generics, status
from rest_framework.views import APIView
from .serializers import BasketItemSerializer, BasketSessionSerializer
from .models import BasketItem, BasketSession
from django.http import JsonResponse  
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
import uuid 


@api_view(http_method_names=["POST"])
def addProduct(request):
    user_id = request.query_params.get("user_id")
    print(user_id)
    if user_id == None:
        user_id = uuid.uuid4()

    print(user_id)
    queryset = BasketSession.objects.filter(user_id=user_id, status='open')
    if queryset.count() != 0:
        
        basket_serializer = BasketSessionSerializer(queryset, many=True) 
        product = request.data["product_id"]
        response = requests.get("http://127.0.0.1:8003/product/basket/?prod_id=%d" % product).json() 
      #  response = requests.get("http://catalog-web:8002/product/basket/?prod_id=%d" % product).json()
        #print(response)
        if  type(response) is dict:
            return Response(status = 404)
        else : 
            basket_session_id = BasketSession.objects.filter(basket_id=basket_serializer.data[0]['basket_id'], status='open').first()
            basket_item = BasketItem.objects.filter(basket_session_id =basket_session_id,  catalog_item_id = product)
            if basket_item.count() != 0:
                basket_item.update(quantity=basket_item.first().quantity+request.data["quantity"])
                basket_item.first().save()
                
            else:

                basket_item = BasketItem()
                basket_item.basket_session_id = BasketSession.objects.filter(basket_id=basket_serializer.data[0]['basket_id'], status='open').first()
                basket_item.catalog_item_id = response[0]['catalog_item_id']
                basket_item.slug = response[0]['slug']
                basket_item.quantity = request.data["quantity"]
                basket_item.save()
            
            return Response(status = 200)

    else:
        basket_session = BasketSession()
        basket_session.user_id = user_id
        basket_session.status = 'open'
        basket_session.save()
        basket_serializer = BasketSessionSerializer(queryset, many=True) 
        queryset2 = BasketSession.objects.filter(user_id=user_id)
        product = request.data["product_id"]
        print("AAAAAA")
       # response = requests.get("http://catalog-web:8002/product/basket/?prod_id=%d" % product).json()
        response = requests.get("http://127.0.0.1:8003/product/basket/?prod_id=%d" % product).json()
        print(response)
        if  type(response) is dict:
            return Response(status = 404)
        else : 
            basket_item = BasketItem()
            basket_item.basket_session_id = BasketSession.objects.filter(basket_id=basket_serializer.data[0]['basket_id'], status='open').first()
            basket_item.catalog_item_id = response[0]['catalog_item_id']
            basket_item.slug = response[0]['slug']
            basket_item.quantity = request.data["quantity"]
            basket_item.save()
           
            return Response(status = 200)

@api_view(http_method_names=["POST"])
def removeItem(request):
    user_id = request.query_params.get("user_id")
    if user_id == None:
        return Response(status=400)
    queryset = BasketSession.objects.filter(user_id=user_id, status='open')
    if queryset.count() != 0:
        basket_serializer = BasketSessionSerializer(queryset, many=True) 
        catalog_item_id = request.data["product_id"]
        basket_id = BasketSession.objects.filter(basket_id=basket_serializer.data[0]['basket_id'], status='open').first()
        basket_item = BasketItem.objects.filter(basket_session_id =basket_id,  catalog_item_id = catalog_item_id)
        basket_item.delete()
        
        return Response(status = 200)


@api_view(http_method_names=["POST"])
def removeBasket(request):
    user_id = request.query_params.get("user_id")
    if user_id == None:
        return Response(status=400)
    basket = BasketSession.objects.filter(user_id=user_id, status='open')
    if basket.count() != 0:
        basket.delete()
        
        return Response(status = 200)
        

@api_view(http_method_names=["POST"])
def changeQuantity(request):
    user_id = request.query_params.get("user_id")
    if user_id == None:
        return Response(status=400)
    
    queryset = BasketSession.objects.filter(user_id=user_id, status='open')
    if queryset.count() != 0:
        basket_serializer = BasketSessionSerializer(queryset, many=True) 
        catalog_item_id = request.data["product_id"]
        quantity = request.data["quantity"]
        basket_id = BasketSession.objects.filter(basket_id=basket_serializer.data[0]['basket_id'], status='open').first()
        basket_item = BasketItem.objects.filter(basket_session_id =basket_id,  catalog_item_id = catalog_item_id)
        if basket_item.count() != 0:
                basket_item.update(quantity=quantity)
                basket_item.first().save()

        
        if basket_item.first().quantity == 0:
            basket_item.delete()
            
    return Response(status = 200)



@api_view(http_method_names=["GET"])
def basket(request):
    user_id = request.query_params.get("user_id")
    print(user_id)
    if user_id == None:
        user_id = uuid.uuid4()
    queryset = BasketSession.objects.filter(user_id=user_id, status='open')
    
    basket_session_serializer = BasketSessionSerializer(queryset, many=True) 
    
    if queryset.count() == 0:
        return Response( status = 404)
    else :
        return Response( basket_session_serializer.data, status = 200)



@api_view(http_method_names=["GET"])
def createOrder(request):
    if request.method == 'GET':
        basket_id = BasketSession.objects.filter(user_id=request.query_params.get("user_id"), status='open').first()
        basket_items = BasketItem.objects.filter(basket_session_id =basket_id)
        if basket_items.count() != 0:
            serializer_class = BasketItemSerializer(basket_items, many=True)
            return Response(serializer_class.data, status=200)
        else:
            return Response({"message": "Not found"}, status=404)






'''
{
"product_id": 1,
"quantity": 2
}
'''

