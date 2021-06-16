from django.contrib import admin

from .forms import CatalogItemForm
from .models import Opinion, Category, ProductImage, CatalogItem


class CatalogItemAdmin(admin.ModelAdmin):
    form = CatalogItemForm


admin.site.register(ProductImage, CatalogItemAdmin)

admin.site.register(CatalogItem)
admin.site.register(Opinion)
admin.site.register(Category)
