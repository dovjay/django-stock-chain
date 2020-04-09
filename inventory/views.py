from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .forms import ProductForm, VarianProductForm, CategoryForm
from .models import Category, Product, VarianProduct
from account.models import Warehouse

# Create your views here.
def dashboard(request):
    return render(request, 'inventory/dashboard.html')

def products(request):
    warehouses = Warehouse.objects.all()
    products = Product.objects.all()
    context = {
        'products': products,
        'warehouses': warehouses
    }
    return render(request, 'inventory/products.html', context)

class CreateProduct(CreateView):
    model = Product
    form_class = ProductForm
    template_name_suffix = '_form'
    success_url = reverse_lazy('inventory-products')

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
        product_name = product.name
        varian_products = VarianProduct.objects.filter(product=product)
    else:
        product_name = ''
        varian_products = None

    products = Product.objects.all()
    context = {
        'products': products,
        'varian_products': varian_products,
        'product_name': product_name
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
    success_url = '/varian-product/'

    def get_success_url(self, **kwargs):
        url = reverse_lazy('inventory-varian-product')
        qs = f'product_id={self.object.product.id}'
        success_url = f'{url}?{qs}'
        return success_url

class DeleteVarianProduct(DeleteView):
    model = VarianProduct
    success_url = '/varian-product/'

def invoices(request):
    return render(request, 'inventory/invoices.html')

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