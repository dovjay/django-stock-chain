from django import forms
from .models import Product, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'image', 'sku', 'category', 'stock', 'supplier', 'note']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = []