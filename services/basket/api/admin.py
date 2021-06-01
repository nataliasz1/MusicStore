from django.contrib import admin

from .models import BasketItem, BasketSession

admin.site.register(BasketItem)
admin.site.register(BasketSession)
