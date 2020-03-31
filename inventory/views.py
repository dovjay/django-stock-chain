from django.shortcuts import render
from .forms import ProductForm
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
