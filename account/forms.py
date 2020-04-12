from django import forms
from .models import PermissionWarehouse, Warehouse, Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ['owner']
        