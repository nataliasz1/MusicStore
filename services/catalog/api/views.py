import json
import os
import uuid
from statistics import median

import pyrebase
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.settings import BASE_DIR
from .models import CatalogItem, Category, Opinion
from .serializers import CatalogItemSerializer, CategorySerializer, OpinionSerializer
from .settings import FIREBASE_CONFIG_FILE

conf = ''

FIREBASE_FILE_PATH = os.path.join(BASE_DIR, FIREBASE_CONFIG_FILE)
with open(FIREBASE_FILE_PATH, "r") as read_file:
    j = json.load(read_file)

config = j
firebase = pyrebase.initialize_app(config)
storage = firebase.storage()


@api_view(http_method_names=["GET"])
def getItems(request):
    if request.method == 'GET':
        queryset = CatalogItem.objects.all()
        if queryset.count() != 0:
            serializer_class = CatalogItemSerializer(queryset, many=True)

            return Response(serializer_class.data, status=200)
        else:
            return Response(status=200)


@api_view(http_method_names=["GET"])
def getItem(request, slug):
    if request.method == 'GET':
        lookup_field = 'slug'
        queryset = CatalogItem.objects.filter(slug=slug)
        if queryset.count() != 0:
            serializer_class = CatalogItemSerializer(queryset, many=True)

            return Response(serializer_class.data, status=200)
        else:
            return Response(status=200)


@api_view(http_method_names=["GET"])
def getCategories(request):
    if request.method == 'GET':
        queryset = Category.objects.all()
        if queryset.count() != 0:
            serializer_class = CategorySerializer(queryset, many=True)

            return Response(serializer_class.data, status=200)
        else:
            return Response(status=404)


@api_view(http_method_names=["GET"])
def getCategoryItems(request, slug):
    if request.method == 'GET':
        lookup_field = 'slug'
        queryset = Category.objects.filter(slug=slug)
        if queryset.count() == 0:
            return Response(status=404)
        else:
            products = CatalogItem.objects.filter(
                category__in=Category.objects.get(slug=slug).get_descendants(include_self=True)
            )
            if products.count() != 0:
                serializer_class = CatalogItemSerializer(products, many=True)

                return Response(serializer_class.data, status=200)

            else:
                return Response(status=404)


@api_view(http_method_names=["GET"])
def addToBasket(request):
    if request.method == 'GET':
        queryset = CatalogItem.objects.filter(catalog_item_id=request.query_params.get("prod_id"))
        if queryset.count() != 0:
            serializer_class = CatalogItemSerializer(queryset, many=True)
            return Response(serializer_class.data, status=200)
        else:
            return Response({"message": "Not found"}, status=404)


@api_view(http_method_names=["POST"])
def addOpinion(request):
    user_id = request.user
    if user_id == None:
        user_id = uuid
    opinion = Opinion()
    opinion.product_id = request.data["prod_id"]
    opinion.text = request.data['text']
    opinion.stars = request.data['stars']
    opinion.user_id = user_id
    opinion.save()
    querysetItem = CatalogItem.objects.filter(catalog_item_id=request.data["prod_id"])
    print(request.data["prod_id"])
    querysetOpinion = Opinion.objects.filter(product_id=request.data["prod_id"])
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
def getOpinionsPerProduct(request):
    if request.method == 'GET':
        queryset = Opinion.objects.filter(product=request.query_params.get("prod_id"))
        if queryset.count() != 0:
            serializer_class = OpinionSerializer(queryset, many=True)

            return Response(serializer_class.data, status=200)
        else:
            return Response(status=404)


@api_view(http_method_names=["GET"])
def getOpinionPerId(request):
    if request.method == 'GET':
        queryset = Opinion.objects.filter(opinion_id=request.query_params.get("id"))
        if queryset.count() != 0:
            serializer_class = OpinionSerializer(queryset, many=True)

            return Response(serializer_class.data, status=200)
        else:

            return Response(status=404)


@api_view(http_method_names=["GET"])
def getOpinionsPerUser(request):
    if request.method == 'GET':
        queryset = Opinion.objects.filter(user_id=request.query_params.get("usr_id"))
        if queryset.count() != 0:
            serializer_class = OpinionSerializer(queryset, many=True)

            return Response(serializer_class.data, status=200)
        else:
            return Response(status=404)
