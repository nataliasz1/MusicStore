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
    user_id = request.user
    if user_id == None:
        user_id = uuid

    print(user_id)
    queryset = BasketSession.objects.filter(user_id=user_id, status='open')
    if queryset.count() != 0:
        
        basket_serializer = BasketSessionSerializer(queryset, many=True) 
        product = request.data["product_id"]
        
        response = requests.get("http://127.0.0.1:8002/product/basket/?prod_id=%d" % product).json()
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
        response = requests.get("http://127.0.0.1:8002/product/basket/?prod_id=%d" % product).json()
        print(response)
        if  type(response) is dict:
            return Response(status = 404)
        else : 
            basket_item = BasketItem()
            basket_item.basket_session_id = BasketSession.objects.filter(basket_id=basket_serializer.data[0]['basket_id'], status='open').first()
            basket_item.catalog_item_id = response['catalog_item_id']
            basket_item.quantity = request.data["quantity"]
            basket_item.save()
           
            return Response(status = 200)

@api_view(http_method_names=["POST"])
def removeItem(request):
    user_id = request.user
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
    user_id = request.user
    if user_id == None:
        return Response(status=400)
    basket = BasketSession.objects.filter(user_id=user_id, status='open')
    if basket.count() != 0:
        basket.delete()
        
        return Response(status = 200)
        

@api_view(http_method_names=["POST"])
def changeQuantity(request):
    user_id = request.user
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
    return Response(status = 200)



@api_view(http_method_names=["GET"])
def basket(request):
    user_id = request.user
    if user_id == None:
        user_id = uuid
    queryset = BasketSession.objects.filter(user_id=user_id, status='open')
    
    basket_session_serializer = BasketSessionSerializer(queryset, many=True) 
    print(basket_session_serializer.data[0]['basket_id'])
    if queryset.count() == 0:
        return Response( status = 404)
    else :
        products = BasketItem.objects.filter(
                basket_session_id=BasketSession.objects.filter(basket_id=basket_session_serializer.data[0]['basket_id'], status='open').first()
        )
        if products.count() != 0 :
                
                print(products.first())
                serializer_class = BasketItemSerializer(products, many=True)
                print(serializer_class.data)
                
                return Response(serializer_class.data, status = 200)

        else : return Response(status = 404)



'''
{
"product_id": 2,
"quantity": 2
}
'''

