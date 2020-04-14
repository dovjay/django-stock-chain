from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PermissionWarehouse, Warehouse, Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ['owner']
        
class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        exclude = ['owner']

class PermissionWarehouseForm(forms.ModelForm):
    class Meta:
        model = PermissionWarehouse
        exclude = []

class AccountForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    is_superuser = forms.BooleanField(required=False)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'is_superuser')