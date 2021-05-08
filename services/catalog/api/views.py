from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import CatalogItem
from .serializers import CatalogItemSerializer


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


class CatalogItemViewSet(ModelViewSet):
    queryset = CatalogItem.objects.all().order_by('name')
    serializer_class = CatalogItemSerializer
