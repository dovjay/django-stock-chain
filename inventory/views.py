from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'inventory/dashboard.html')

def products(request):
    return render(request, 'inventory/products.html')

def invoices(request):
    return render(request, 'inventory/invoices.html')
