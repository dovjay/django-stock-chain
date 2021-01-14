from django import forms
from bootstrap_modal_forms.forms import BSModalModelForm
from .models import Product, VarianProduct, Category
from account.models import Contact

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['warehouse', 'supplier']
        labels = {
            'name': 'Nama',
            'sku': 'Kode',
            'category': 'Kategori',
            'image': 'Gambar'
        }

    supplier = forms.ModelChoiceField(queryset=Contact.objects.filter(is_supplier=True), required=False)

class ProductSUForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['supplier']
        labels = {
            'name': 'Nama',
            'sku': 'Kode',
            'category': 'Kategori',
            'image': 'Gambar',
            'warehouse': 'Gudang/Toko'
        }

    supplier = forms.ModelChoiceField(queryset=Contact.objects.filter(is_supplier=True), required=False)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {
            'name': 'Nama'
        }

class VarianProductForm(forms.ModelForm):
    class Meta:
        model = VarianProduct
        exclude = ['product']
        labels = {
            'size': 'Ukuran',
            'product_type': 'Tipe Produk',
            'product': 'Produk',
            'stock': 'Stok',
            'sell_price': 'Harga Jual',
            'buy_price': 'Harga Beli'
        }

class VarianProductBSForm(BSModalModelForm):
    class Meta:
        model = VarianProduct
        exclude = ['product']
        labels = {
            'size': 'Ukuran',
            'product_type': 'Tipe Produk',
            'product': 'Produk',
            'stock': 'Stok',
            'sell_price': 'Harga Jual',
            'buy_price': 'Harga Beli'
        }