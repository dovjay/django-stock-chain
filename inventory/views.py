from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q, Sum
from django.db.models.functions import Trim
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProductForm, ProductSUForm, VarianProductForm, CategoryForm
from .models import Category, Product, VarianProduct
from account.models import Warehouse, PermissionWarehouse
from invoice.models import InvoiceItem, Invoice

# Create your views here.
@login_required
def dashboard(request):
    total_product = Product.objects.all().count()

    assets = VarianProduct.objects.all()
    total_assets = 0
    for asset in assets:
        total_assets += asset.buy_price

    sold_products = InvoiceItem.objects.all()
    total_profit = 0
    for product in sold_products:
        total_profit += product.get_profit
    
    products = InvoiceItem.objects.values('varian_product__product__name', 'varian_product__product__sku').order_by('varian_product__product__sku').annotate(total_order=Sum('quantity'))[:10]

    context = {
        'total_product': total_product,
        'total_assets': total_assets,
        'total_profit': total_profit,
        'products': products
    }
    return render(request, 'inventory/dashboard.html', context)

@login_required
def products(request):
    if request.user.is_superuser:

        if request.GET.get('warehouse_id'):
            warehouse = Warehouse.objects.get(pk=request.GET.get('warehouse_id'))
            warehouses = Warehouse.objects.all()

        else:
            warehouses = Warehouse.objects.all()
            if warehouses:
                warehouse = warehouses[0]
            else:
                return redirect(reverse_lazy('account-create-warehouse'))

        # search
        if request.GET.get('q'):
            query = request.GET.get('q')
            products = Product.objects.filter(Q(warehouse=warehouse), Q(sku__contains=query) | Q(name__contains=query))
        else:
            products = Product.objects.filter(warehouse=warehouse)

    else:
        permission = PermissionWarehouse.objects.get(user=request.user)
        warehouse = Warehouse.objects.get(pk=permission.warehouse.pk)
        warehouses = warehouse

        # search too
        if request.GET.get('q'):
            query = request.GET.get('q')
            products = Product.objects.filter(Q(warehouse=permission.warehouse), Q(sku__contains=query) | Q(name__contains=query))
        else:
            products = Product.objects.filter(warehouse=permission.warehouse)
        
    context = {
        'products': products,
        'warehouses': warehouses,
        'warehouse': warehouse,
        'warehouse_name': warehouse.name
    }

    response = render(request, 'inventory/products.html', context)
    response.set_cookie('warehouse_id', warehouse.id)
    return response

class CreateProduct(LoginRequiredMixin, CreateView):
    model = Product
    template_name_suffix = '_form'

    def get_form_class(self):
        if self.request.user.is_superuser:
            return ProductSUForm
        return ProductForm

    def form_valid(self, form):
        if not self.request.user.is_superuser:
            permission = PermissionWarehouse.objects.get(user=self.request.user)
            form.instance.warehouse = permission.warehouse
        return super(CreateProduct, self).form_valid(form)

    def get_success_url(self, **kwargs):
        url = reverse_lazy('inventory-varian-product')
        qs = f'product_id={self.object.id}'
        success_url = f'{url}?{qs}'
        return success_url

class UpdateProduct(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name_suffix = '_form'
    success_url = reverse_lazy('inventory-products')

class DeleteProduct(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('inventory-products')

@login_required
def varian_product(request):
    if request.GET.get('product_id'):
        product = Product.objects.get(pk=request.GET.get('product_id'))
        product_sku = product.sku
        varian_products = VarianProduct.objects.filter(product=product)
    else:
        product_sku = ''
        varian_products = None

    try:
        warehouse = Warehouse.objects.get(pk=request.COOKIES.get('warehouse_id'))
    except:
        return redirect(reverse_lazy('account-create-warehouse'))

    products = Product.objects.filter(warehouse=warehouse)

    context = {
        'products': products,
        'varian_products': varian_products,
        'product_sku': product_sku,
        'warehouse': warehouse
    }
    return render(request, 'inventory/varian_product.html', context)

class CreateVarianProduct(LoginRequiredMixin, CreateView):
    model = VarianProduct
    form_class = VarianProductForm
    template_name_suffix = '_form'

    def get_success_url(self, **kwargs):
        url = reverse_lazy('inventory-varian-product')
        qs = f'product_id={self.object.product.id}'
        success_url = f'{url}?{qs}'
        return success_url

    def form_valid(self, form, *args, **kwargs):
        try:
            form.instance.product = Product.objects.get(id=self.kwargs.get('project_id'))
        except:
            return False
        return super(CreateVarianProduct, self).form_valid(form)

class UpdateVarianProduct(LoginRequiredMixin, UpdateView):
    model = VarianProduct
    form_class = VarianProductForm
    template_name_suffix = '_form'

    def get_success_url(self, **kwargs):
        url = reverse_lazy('inventory-varian-product')
        qs = f'product_id={self.object.product.id}'
        success_url = f'{url}?{qs}'
        return success_url

class DeleteVarianProduct(LoginRequiredMixin, DeleteView):
    model = VarianProduct
    success_url = reverse_lazy('inventory-varian-product')

@login_required
def categories(request):
    if request.GET.get('q'):
        query = request.GET.get('q')
        categories = Category.objects.filter(name__contains=query)
    else:
        categories = Category.objects.all()

    context = {
        'categories': categories
    }
    return render(request, 'inventory/categories.html', context)

class CreateCategory(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name_suffix =  '_form'
    success_url = reverse_lazy('inventory-categories')

class UpdateCategory(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name_suffix = '_form'
    success_url = reverse_lazy('inventory-categories')
    
class DeleteCategory(LoginRequiredMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('inventory-categories')