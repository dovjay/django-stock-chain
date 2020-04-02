from django.db import models
from account.models import Contact, Warehouse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

class Product(models.Model):
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=1)
    stock = models.PositiveIntegerField(default=0)
    note = models.TextField(blank=True)
    image = models.ImageField(upload_to='product_images/')
    supplier = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True, blank=True)
    last_modified = models.DateField(auto_now=True)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

class Varian(models.Model):
    ATTR_CHOICE = [
        ("WARNA", "Warna"),
        ("UKURAN", "Ukuran"),
        ("BERAT", "Berat")
    ]

    attribute = models.CharField(max_length=10, choices=ATTR_CHOICE, default="UKURAN")
    value = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.attribute}: {self.value}'

class VarianProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    varian = models.ForeignKey(Varian, on_delete=models.CASCADE)
    sell_price = models.PositiveIntegerField(default=0, blank=True, null=True)
    buy_price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.product} - {self.varian}'
