from django import forms
from .models import Invoice, InvoiceItem
from account.models import Contact

class InvoiceForm(forms.ModelForm):
    customer = forms.ModelChoiceField(queryset=Contact.objects.filter(is_customer=True), required=False)
    class Meta:
        model = Invoice
        exclude = ['created', 'updated', 'customer', 'warehouse']

class InvoiceItemForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        exclude = ['invoice']