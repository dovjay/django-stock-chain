from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .forms import ProductForm, CategoryForm
from .models import Category

# Create your views here.
def dashboard(request):
    return render(request, 'inventory/dashboard.html')

def products(request):
    return render(request, 'inventory/products.html')

def invoices(request):
    return render(request, 'inventory/invoices.html')

def varian_product(request):
    return render(request, 'inventory/varian_product.html')

def product_form(request):
    if request.method == "POST":
        pass
    else:
        form = ProductForm()
        context = {
            'form': form
        }
        return render(request, 'inventory/product_form.html', context)

def categories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'inventory/categories.html', context)

class CreateCategory(CreateView):
    model = Category
    form_class = CategoryForm
    template_name_suffix =  '_modal_form'
    success_url = '/categories/'

class UpdateCategory(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name_suffix = '_modal_form'
    success_url = '/categories/'
    
class DeleteCategory(DeleteView):
    model = Category
    success_url = '/categories/'