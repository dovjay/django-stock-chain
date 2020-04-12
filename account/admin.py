from django.contrib import admin
from .models import Warehouse, Contact, PermissionWarehouse

# Register your models here.
admin.site.register(Warehouse)
admin.site.register(Contact)
admin.site.register(PermissionWarehouse)