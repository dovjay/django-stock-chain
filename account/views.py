from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import PermissionWarehouse, Warehouse, Contact
from .forms import ContactForm, PermissionWarehouseForm, WarehouseForm, AccountForm

# Create your views here.
@login_required
def contacts(request):
    # search contact by name, phone, email, is_customer, and is_supplier
    if request.GET.get('q'):
        query = request.GET.get('q')
        contacts = Contact.objects.filter(Q(name__contains=query) | Q(phone__contains=query) | Q(email__contains=query))
    elif request.GET.get('is_customer'):
        contacts = Contact.objects.filter(is_customer=True)
    elif request.GET.get('is_supplier'):
        contacts = Contact.objects.filter(is_supplier=True)
    else:
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
class CreateContact(LoginRequiredMixin, CreateView):
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

class UpdateContact(LoginRequiredMixin, UpdateView):
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
        return super(UpdateContact, self).form_valid(form)

class DeleteContact(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Contact
    success_url = reverse_lazy('account-contacts')

    def test_func(self):
        return self.request.user.is_superuser

@login_required
def manage_accounts(request):
    if request.user.is_superuser:
        warehouses = Warehouse.objects.all()
        permissions = PermissionWarehouse.objects.all()
        accounts = User.objects.all()
        context = {
            'warehouses': warehouses,
            'permissions': permissions,
            'accounts': accounts
        }
        return render(request, 'account/accounts.html', context)
    else:
        return HttpResponse("403 Forbidden")


# Warehouse Controller
class CreateWarehouse(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Warehouse
    form_class = WarehouseForm
    template_name_suffix = '_form'
    success_url = reverse_lazy('account-manage-accounts')

    def test_func(self):
        return self.request.user.is_superuser

    def form_valid(self, form, *args, **kwargs):
        form.instance.owner = self.request.user
        return super(CreateWarehouse, self).form_valid(form)

class UpdateWarehouse(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Warehouse
    form_class = WarehouseForm
    template_name_suffix = '_form'
    success_url = reverse_lazy('account-manage-accounts')

    def test_func(self):
        return self.request.user.is_superuser

class DeleteWarehouse(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Warehouse
    success_url = reverse_lazy('account-manage-accounts')

    def test_func(self):
        return self.request.user.is_superuser

# Permission Controller
class CreatePermissionWarehouse(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = PermissionWarehouse
    form_class = PermissionWarehouseForm
    template_name_suffix = '_form'
    success_url = reverse_lazy('account-manage-accounts')

    def test_func(self):
        return self.request.user.is_superuser

class DeletePermissionWarehouse(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = PermissionWarehouse
    success_url = reverse_lazy('account-manage-accounts')

    def test_func(self):
        return self.request.user.is_superuser

# Account Controller
class CreateAccount(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = User
    form_class = AccountForm
    template_name = 'account/account_form.html'
    success_url = reverse_lazy('account-manage-accounts')

    def test_func(self):
        return self.request.user.is_superuser

class UpdateAccount(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    form_class = AccountForm
    template_name = 'account/account_form.html'
    success_url = reverse_lazy('account-manage-accounts')

    def test_func(self):
        return self.request.user.is_superuser

class DeleteAccount(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    success_url = reverse_lazy('account-manage-accounts')

    def test_func(self):
        return self.request.user.is_superuser