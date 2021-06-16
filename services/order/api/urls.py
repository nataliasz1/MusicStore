"""
Order_service URL Configuration

"""

# Uncomment next two lines to enable admin:
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework import routers
from . import views

from .views import OrderViewSet, PaymentViewSet, OrderItemViewSet

router = routers.DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'orderitems', OrderItemViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('api-doc/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'api/openapi-schema.yml'}
    ), name='swagger-ui'),
]

urlpatterns += [
    path('orders/user-id/<user_id>', OrderViewSet.as_view({'get': 'get_orders_per_user'})),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('order/', views.create_order)
]
