from django.http import HttpResponse
from rest_framework import views, viewsets, generics
from rest_framework.views import APIView
from .serializers import CatalogItemSerializer
from .models import CatalogItem
from django.http import JsonResponse  

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


class CatalogItemViewSet(generics.ListAPIView):
    queryset = CatalogItem.objects.all().order_by('name')
    serializer_class = CatalogItemSerializer


