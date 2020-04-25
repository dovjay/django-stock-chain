from django import forms
from .models import Invoice, InvoiceItem
from account.models import Contact

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['status', 'customer', 'due', 'paid_date', 'discount', 'notes', 'total']

class InvoiceItemForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        exclude = ['invoice']