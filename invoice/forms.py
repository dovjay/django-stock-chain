from django import forms
from .models import Invoice, InvoiceItem
from account.models import Contact

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['status', 'customer', 'due', 'paid_date', 'discount', 'notes', 'total']
        labels = {
            'due': 'Jatuh Tempo',
            'paid_date': 'Tanggal Bayar',
            'discount': 'Diskon'
        }

class InvoiceItemForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        exclude = ['invoice']
        labels = {
            'varian_product': 'Varian Produk',
            'name': 'Nama',
            'sku':  'Kode',
            'price': 'Harga'
        } 