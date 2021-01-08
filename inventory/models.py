from django.db import models
from account.models import Contact, Warehouse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

class Product(models.Model):
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=1)
    note = models.TextField(blank=True)
    image = models.ImageField(default='default.jpg', blank=True, upload_to='product_images/')
    supplier = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True, blank=True)
    last_modified = models.DateField(auto_now=True)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

class VarianProduct(models.Model):
    ATTR_CHOICE = [
        ("1-3", "1-3"),
        ("4-6", "4-6"),
        ("8-10", "8-10"),
        ("5-15", "5-15"),
        ("7-15", "7-15"),
        ("11-13", "11-13"),
        ("100-140", "100-140"),
        ("150-180", "150-180")
    ]
    size = models.CharField(max_length=20, default="1-3")
    seri = models.PositiveSmallIntegerField(default=1, help_text="Potongan seri")
    product_type = models.CharField(max_length=100, help_text="Bisa input warna, atau tipe khusus")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(default=0)
    sell_price = models.PositiveIntegerField(default=0, blank=True, null=True)
    buy_price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.product} - {self.size} - {self.product_type}'
