from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    phone = PhoneNumberField(blank=True)
    email = models.EmailField(max_length=100, blank=True)
    company = models.CharField(max_length=200, blank=True)
    is_customer = models.BooleanField(default=True)
    is_supplier = models.BooleanField(default=True)
    address1 = models.CharField(max_length=50, blank=True)
    address2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    province = models.CharField(max_length=50, blank=True)
    nation = models.CharField(max_length=50, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

class Warehouse(models.Model):
    name = models.CharField(max_length=200)
    address1 = models.CharField(max_length=50, blank=True)
    address2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    province = models.CharField(max_length=50, blank=True)
    nation = models.CharField(max_length=50, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

class PermissionWarehouse(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    warehouse = models.OneToOneField(Warehouse, on_delete=models.CASCADE)
