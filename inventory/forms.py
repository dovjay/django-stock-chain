from django import forms
from .models import Product
from django.core.validators import RegexValidator

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'image', 'sku', 'category', 'stock', 'supplier', 'note']