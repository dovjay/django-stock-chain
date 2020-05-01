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
    note = models.TextField(blank=True)
    image = models.ImageField(default='default_product.jpg', blank=True, upload_to='product_images/')
    supplier = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True, blank=True)
    last_modified = models.DateField(auto_now=True)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

class VarianProduct(models.Model):
    ATTR_CHOICE = [
        ("UKURAN", "Ukuran"),
        ("WARNA", "Warna"),
        ("BERAT", "Berat")
    ]
    varian_attribute = models.CharField(max_length=10, choices=ATTR_CHOICE, default="UKURAN")
    varian_value = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(default=0)
    sell_price = models.PositiveIntegerField(default=0, blank=True, null=True)
    buy_price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.product} - {self.varian_attribute}: {self.varian_value}'
