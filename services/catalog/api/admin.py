from django.contrib import admin

from .models import CatalogItem, Opinion, Category, ProductImage

from .forms import MyProductImage

class MyModelAdmin(admin.ModelAdmin):
    form = MyProductImage
admin.site.register(ProductImage, MyModelAdmin)

admin.site.register(CatalogItem)
admin.site.register(Opinion)
admin.site.register(Category)
#admin.site.register(ProductImage)

