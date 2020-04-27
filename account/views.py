from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import PermissionWarehouse, Warehouse, Contact
from .forms import ContactForm, PermissionWarehouseForm, WarehouseForm, AccountForm

# Create your views here.
def contacts(request):
    contacts = Contact.objects.all()
    customer_count = Contact.objects.filter(is_customer=True).count()
    supplier_count = Contact.objects.filter(is_supplier=True).count()
    context = {
        'contacts': contacts,
        'customer_count': customer_count,
        'supplier_count': supplier_count
    }
    return render(request, 'account/contacts.html', context)

# Contact Controller
class CreateContact(CreateView):
    model = Contact
    form_class = ContactForm
    template_name_suffix = '_form'
    success_url = reverse_lazy('account-contacts')

    def form_valid(self, form, *args, **kwargs):
        if self.request.user.is_superuser:
            form.instance.owner = self.request.user
        else:
            permission = get_object_or_404(PermissionWarehouse, user=self.request.user)
            form.instance.owner = permission.warehouse.owner
        return super(CreateContact, self).form_valid(form)

class UpdateContact(UpdateView):
    model = Contact
    form_class = ContactForm
    template_name_suffix = '_form'
    success_url = reverse_lazy('account-contacts')

class DeleteContact(DeleteView):
    model = Contact
    success_url = reverse_lazy('account-contacts')

def manage_accounts(request):
    warehouses = Warehouse.objects.all()
    permissions = PermissionWarehouse.objects.all()
    accounts = User.objects.all()
    context = {
        'warehouses': warehouses,
        'permissions': permissions,
        'accounts': accounts
    }
    return render(request, 'account/accounts.html', context)

# Warehouse Controller
class CreateWarehouse(UserPassesTestMixin, CreateView):
    model = Warehouse
    form_class = WarehouseForm
    template_name_suffix = '_form'
    success_url = reverse_lazy('account-manage-accounts')

    def test_func(self):
        return self.request.user.is_superuser

    def form_valid(self, form, *args, **kwargs):
        form.instance.owner = self.request.user
        return super(CreateWarehouse, self).form_valid(form)

class UpdateWarehouse(UserPassesTestMixin, UpdateView):
    model = Warehouse
    form_class = WarehouseForm
    template_name_suffix = '_form'
    success_url = reverse_lazy('account-manage-accounts')

    def test_func(self):
        return self.request.user.is_superuser

class DeleteWarehouse(UserPassesTestMixin, DeleteView):
    model = Warehouse
    success_url = reverse_lazy('account-manage-accounts')

    def test_func(self):
        return self.request.user.is_superuser

# Permission Controller
class CreatePermissionWarehouse(UserPassesTestMixin, CreateView):
    model = PermissionWarehouse
    form_class = PermissionWarehouseForm
    template_name_suffix = '_form'
    success_url = reverse_lazy('account-manage-accounts')

    def test_func(self):
        return self.request.user.is_superuser

class DeletePermissionWarehouse(UserPassesTestMixin, DeleteView):
    model = PermissionWarehouse
    success_url = reverse_lazy('account-manage-accounts')

    def test_func(self):
        return self.request.user.is_superuser

# Account Controller
class CreateAccount(UserPassesTestMixin, CreateView):
    model = User
    form_class = AccountForm
    template_name = 'account/account_form.html'
    success_url = reverse_lazy('account-manage-accounts')

    def test_func(self):
        return self.request.user.is_superuser

class UpdateAccount(UserPassesTestMixin, UpdateView):
    model = User
    form_class = AccountForm
    template_name = 'account/account_form.html'
    success_url = reverse_lazy('account-manage-accounts')

    def test_func(self):
        return self.request.user.is_superuser

class DeleteAccount(UserPassesTestMixin, DeleteView):
    model = User
    success_url = reverse_lazy('account-manage-accounts')

    def test_func(self):
        return self.request.user.is_superuser