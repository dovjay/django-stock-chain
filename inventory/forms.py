from django import forms
from .models import Product, VarianProduct, Category
from account.models import Contact

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['warehouse', 'supplier']

    supplier = forms.ModelChoiceField(queryset=Contact.objects.filter(is_supplier=True), required=False)

class ProductSUForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['supplier']

    supplier = forms.ModelChoiceField(queryset=Contact.objects.filter(is_supplier=True), required=False)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = []

class VarianProductForm(forms.ModelForm):
    class Meta:
        model = VarianProduct
        exclude = ['product']