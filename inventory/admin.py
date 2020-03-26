from django.contrib import admin
from .models import Category, Product, Varian, VarianProduct

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name', 'sku']
    list_display = ('name', 'sku', 'sell_price', 'buy_price', 'stock', 'last_modified')

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Varian)
admin.site.register(VarianProduct)