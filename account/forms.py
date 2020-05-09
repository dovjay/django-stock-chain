from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PermissionWarehouse, Warehouse, Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ['owner']
        labels = {
            'name': 'Nama',
            'phone': 'Telp.',
            'company': 'Perusahaan',
            'is_customer': 'Seorang Customer',
            'is_supplier': 'Seorang Supplier',
            'address1': 'Alamat 1',
            'address2': 'Alamat 2',
            'city': 'Kota',
            'province': 'Provinsi',
            'nation': 'Negara'
        }
        
class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        exclude = ['owner']
        labels = {
            'name': 'Nama',
            'image': 'Gambar',
            'address1': 'Alamat 1',
            'address2': 'Alamat 2',
            'city': 'Kota',
            'province': 'Provinsi',
            'nation': 'Negara'
        }

class PermissionWarehouseForm(forms.ModelForm):
    class Meta:
        model = PermissionWarehouse
        exclude = []
        labels = {
            'warehouse': 'Gudang/Toko'
        }

class AccountForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Opsional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Opsional.')
    email = forms.EmailField(max_length=254, help_text='Wajib! Harap memasukkan alamat email.')
    is_superuser = forms.BooleanField(required=False)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'is_superuser')
        labels = {
            'first_name': 'Nama Depan',
            'last_name': 'Nama Belakang',
            'is_superuser': 'Seorang Superuser'
        }