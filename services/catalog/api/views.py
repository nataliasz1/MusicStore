from django.http import HttpResponse
from rest_framework import views, viewsets, generics
from rest_framework.views import APIView
from .serializers import CatalogItemSerializer, CategorySerializer, OpinionSerializer
from .models import CatalogItem, Category, Opinion
from django.http import JsonResponse  
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from statistics import median


def index(request):
    return HttpResponse("homepage")

def login(request):
    return HttpResponse("login page")

def profile(request):
    return HttpResponse('profile page')

def catalog(request):
    return HttpResponse('catalog page')


class HomeView(APIView):  

 def get(self, request, format=None):
    return JsonResponse({"message":
    'HELLO WORLD FROM DJANGO AND DOCKER'}) 


class CatalogViewSet(generics.ListAPIView):
    queryset = CatalogItem.objects.all().order_by('name')
    serializer_class = CatalogItemSerializer


@api_view(http_method_names=["GET"])
def showItem(request, slug):
    if request.method == 'GET':
        lookup_field = 'slug'        
        queryset = CatalogItem.objects.filter(slug=slug)
        if queryset.count() != 0 :
            serializer_class = CatalogItemSerializer(queryset, many=True)
            return Response(serializer_class.data, status = 200)
        else:
            return Response( status = 404)
        


@api_view(http_method_names=["GET"])
def showCategoryItems(request, slug):
    if request.method == 'GET':
        lookup_field = 'slug'        
        queryset = Category.objects.filter(slug=slug)
        if queryset.count() == 0:
            return Response( status = 404)
        else :
            products = CatalogItem.objects.filter(
                category__in=Category.objects.get(slug=slug).get_descendants(include_self=True)
        )
            if products.count() != 0 :
                serializer_class = CatalogItemSerializer(products, many=True)
                
                return Response(serializer_class.data, status = 200)
            
            else:
                return Response( status = 404)
            
@api_view(http_method_names=["GET"])
def addToBasket(request):
    if request.method == 'GET':
        queryset = CatalogItem.objects.filter(catalog_item_id=request.query_params.get("prod_id"))
        if queryset.count() != 0 :
            serializer_class = CatalogItemSerializer(queryset, many=True)
            return Response(  serializer_class.data, status = 200)
        else:
            return Response( {"message": "Not found"}, status = 404)

    

@api_view(http_method_names=["POST"])
def addOpinion(request):
    
    
    opinion = Opinion()
    opinion.product_id = request.query_params.get("prod_id")
    opinion.text = request.data['text']
    opinion.stars = request.data['stars']
    opinion.save()
    querysetItem = CatalogItem.objects.filter(catalog_item_id=request.query_params.get("prod_id"))
    querysetOpinion = Opinion.objects.filter(product_id=request.query_params.get("prod_id"))
    print(querysetOpinion.count())
    list_med = []
    for o in querysetOpinion:
        list_med.append(o.stars)
    result = median(list_med)
    print(result)
    querysetItem.update(stars=result)
    querysetItem.first().save()

    return Response(status=200)


@api_view(http_method_names=["GET"])
def getOpinion(request):
    if request.method == 'GET':
        queryset = Opinion.objects.filter(product_id=request.query_params.get("prod_id"))
        if queryset.count() != 0 :
            serializer_class = OpinionSerializer(queryset, many=True)

            return Response(serializer_class.data, status = 200)
        else:
            return Response( status = 404)
        



