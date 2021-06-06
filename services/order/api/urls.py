"""
Order_service URL Configuration

"""

# Uncomment next two lines to enable admin:
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'orders', views.OrderViewSet)
router.register(r'orderitems', views.OrderItemViewSet)
router.register(r'payments', views.PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
