from django.contrib import admin
from .models import Product, ProductCategory

class AdminProductCategory(admin.ModelAdmin):
    readonly_fields = ('updated', 'created')

class AdminShopProduct(admin.ModelAdmin):
    readonly_fields = ('updated', 'created')

admin.site.register(Product, AdminShopProduct)
admin.site.register(ProductCategory, AdminProductCategory)