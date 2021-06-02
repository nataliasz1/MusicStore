"""catalog_service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers


#router = routers.DefaultRouter()
#router.register(r'catalog', views.CatalogItemViewSet.as_view())

urlpatterns = [
    path('admin/', admin.site.urls),
  #  path('', views.index, name = 'index'),
   # path('', include(router.urls)),
  #  path('/api', include(router.urls)),
    path("", views.getItems),
    path("product/<slug:slug>", views.getItem),
    path("categories/", views.getCategories),
     path("category/<slug:slug>", views.getCategoryItems),
     path("product/basket/", views.addToBasket),
     path("opinion/add/", views.addOpinion),
     path("opinionProd/", views.getOpinionsPerProduct),
     path("opinionId/", views.getOpinionPerId),
     path("opinionUsr/", views.getOpinionsPerUser),
     path('product/images/<int:catalog_item_id>/', views.ProductImageList().as_view()),


   

]
