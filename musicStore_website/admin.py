from django.contrib import admin
from .models import CatalogItem, Opinion, Category
from mptt.admin import MPTTModelAdmin

admin.site.register(CatalogItem)
admin.site.register(Opinion)
admin.site.register(Category)