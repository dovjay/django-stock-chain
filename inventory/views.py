from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .forms import ProductForm, ProductSUForm, VarianProductForm, CategoryForm
from .models import Category, Product, VarianProduct
from account.models import Warehouse, PermissionWarehouse

# Create your views here.
def dashboard(request):
    return render(request, 'inventory/dashboard.html')

def products(request):
    if request.user.is_superuser:

        if request.GET.get('warehouse_id'):
            warehouse = Warehouse.objects.get(pk=request.GET.get('warehouse_id'))
            warehouses = Warehouse.objects.all()

        else:
            warehouses = Warehouse.objects.all()
            warehouse = warehouses[0]

        products = Product.objects.filter(warehouse=warehouse)

    else:
        permission = PermissionWarehouse.objects.get(user=request.user)
        products = Product.objects.filter(warehouse=permission.warehouse)
        warehouse = Warehouse.objects.get(pk=permission.warehouse.pk)
        warehouses = warehouse
        
    context = {
        'products': products,
        'warehouses': warehouses,
        'warehouse': warehouse,
        'warehouse_name': warehouse.name
    }

    response = render(request, 'inventory/products.html', context)
    response.set_cookie('warehouse_id', warehouse.id)
    return response

class CreateProduct(CreateView):
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

class UpdateProduct(UpdateView):
    model = Product
    form_class = ProductForm
    template_name_suffix = '_form'
    success_url = reverse_lazy('inventory-products')

class DeleteProduct(DeleteView):
    model = Product
    success_url = reverse_lazy('inventory-products')

def varian_product(request):
    if request.GET.get('product_id'):
        product = Product.objects.get(pk=request.GET.get('product_id'))
        product_sku = product.sku
        varian_products = VarianProduct.objects.filter(product=product)
    else:
        product_sku = ''
        varian_products = None

    warehouse = Warehouse.objects.get(pk=request.COOKIES.get('warehouse_id'))
    products = Product.objects.filter(warehouse=warehouse)

    context = {
        'products': products,
        'varian_products': varian_products,
        'product_sku': product_sku,
        'warehouse': warehouse
    }
    return render(request, 'inventory/varian_product.html', context)

class CreateVarianProduct(CreateView):
    model = VarianProduct
    form_class = VarianProductForm
    template_name_suffix = '_form'

    def get_success_url(self, **kwargs):
        url = reverse_lazy('inventory-varian-product')
        qs = f'product_id={self.object.product.id}'
        success_url = f'{url}?{qs}'
        return success_url

    def form_valid(self, form, *args, **kwargs):
        form.instance.product = get_object_or_404(Product, id=self.kwargs.get('project_id'))
        return super(CreateVarianProduct, self).form_valid(form)

class UpdateVarianProduct(UpdateView):
    model = VarianProduct
    form_class = VarianProductForm
    template_name_suffix = '_form'

    def get_success_url(self, **kwargs):
        url = reverse_lazy('inventory-varian-product')
        qs = f'product_id={self.object.product.id}'
        success_url = f'{url}?{qs}'
        return success_url

class DeleteVarianProduct(DeleteView):
    model = VarianProduct
    success_url = reverse_lazy('inventory-varian-product')

def categories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'inventory/categories.html', context)

class CreateCategory(CreateView):
    model = Category
    form_class = CategoryForm
    template_name_suffix =  '_form'
    success_url = reverse_lazy('inventory-categories')

class UpdateCategory(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name_suffix = '_form'
    success_url = reverse_lazy('inventory-categories')
    
class DeleteCategory(DeleteView):
    model = Category
    success_url = reverse_lazy('inventory-categories')