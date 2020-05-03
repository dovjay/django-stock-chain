from django.core.validators import MaxValueValidator
from django.db import models
from inventory.models import VarianProduct
from account.models import Contact, Warehouse
import datetime

def increment_invoice_number():
    last_invoice = Invoice.objects.all().order_by('id').last()
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    if month < 10: month = f'0{now.month}'

    if not last_invoice:
         return f'INV/{year}/{month}/0001'
    invoice_no = last_invoice.invoice_no
    invoice_int = int(invoice_no.split(f'INV/{year}/{month}/')[-1])
    new_invoice_int = invoice_int + 1
    while len(str(new_invoice_int)) < 4:
        new_invoice_int = '0' + str(new_invoice_int)
    new_invoice_no = f'INV/{year}/{month}/' + new_invoice_int
    return new_invoice_no

class Invoice(models.Model):
    STATUS_CHOICE = [
        ("DRAFT", "Draft"),
        ("DEBT", "Debt"),
        ("PAID", "Paid")
    ]
    invoice_no = models.CharField(max_length=100, editable=False, default=increment_invoice_number)
    customer = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default="DRAFT")
    due = models.DateField(blank=True, null=True, help_text='Format: mm-dd-yyyy')
    paid_date = models.DateField(blank=True, null=True, help_text='Format: mm-dd-yyyy')
    total = models.PositiveIntegerField(default=0)
    discount = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(100)])
    notes = models.TextField(blank=True)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True, editable=False)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.invoice_no

    def get_discount(self):
        return round(self.total * (self.discount * 0.01))

    def get_total(self):
        return self.total - self.get_discount()

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    varian_product = models.ForeignKey(VarianProduct, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=200)
    price = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.invoice} - {self.varian_product}'

    def get_subtotal(self):
        return self.price * self.quantity

    def get_profit(self):
        profit = self.varian_product.sell_price - self.varian_product.buy_price
        return profit * quantity