from django.contrib import admin
from .models import Category, Product, VarianProduct

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name', 'sku']
    list_display = ('name', 'sku', 'category', 'last_modified')

class VarianProductAdmin(admin.ModelAdmin):
    list_display = ('varian_attribute', 'varian_value', 'product', 'stock', 'buy_price', 'sell_price')

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(VarianProduct, VarianProductAdmin)