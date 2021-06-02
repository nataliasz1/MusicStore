from django.contrib import admin

from .models import CatalogItem, Opinion, Category, ProductImage

admin.site.register(CatalogItem)
admin.site.register(Opinion)
admin.site.register(Category)
admin.site.register(ProductImage)

