from django import forms
from .models import Product, VarianProduct, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = []

class VarianProductForm(forms.ModelForm):
    class Meta:
        model = VarianProduct
        exclude = ['product']