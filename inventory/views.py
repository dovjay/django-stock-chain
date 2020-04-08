from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .forms import ProductForm, CategoryForm
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
    success_url = '/products/'

class UpdateProduct(UpdateView):
    model = Product
    form_class = ProductForm
    template_name_suffix = '_form'
    success_url = '/products/'

class DeleteProduct(DeleteView):
    model = Product
    success_url = '/products/'

def varian_product(request):
    return render(request, 'inventory/varian_product.html')

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
    success_url = '/categories/'

class UpdateCategory(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name_suffix = '_form'
    success_url = '/categories/'
    
class DeleteCategory(DeleteView):
    model = Category
    success_url = '/categories/'