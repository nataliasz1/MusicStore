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
from django.urls import path

from . import views
from .views import CatalogItemsApiView, CatalogCategoriesListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("products", CatalogItemsApiView.as_view()),
    path("products/<int:item_id>", views.getItem),
    path("categories", CatalogCategoriesListView.as_view()),
    path("category/<slug:slug>", views.getCategoryItems),
    path("product/basket/", views.addToBasket),
    path("opinion/add/", views.addOpinion),
    path("opinionProd/", views.getOpinionsPerProduct),
    path("opinionId/", views.getOpinionPerId),
    path("opinionUsr/", views.getOpinionsPerUser),

]
