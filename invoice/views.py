from django.urls import reverse
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.db.models import F
from .models import Invoice, InvoiceItem
from .forms import InvoiceForm, InvoiceItemForm
from account.models import Warehouse
from inventory.models import VarianProduct, Product
from django.forms.models import model_to_dict

# Create your views here.
def invoices(request):
    if request.user.is_superuser:
        if request.GET.get('warehouse_id'):
            warehouse = Warehouse.objects.get(pk=request.GET.get('warehouse_id'))
            warehouses = Warehouse.objects.all()
            invoices = Invoice.objects.filter(warehouse=warehouse)
        else:
            warehouses = Warehouse.objects.all()
            warehouse = warehouses[0]
            url = reverse('invoice-list')
            qs = f'warehouse_id={warehouse.id}'
            return redirect(f'{url}?{qs}')

    else:
        permission = PermissionWarehouse.objects.get(user=request.user)
        warehouse = Warehouse.objects.get(warehouse=permission.warehouse)
        invoices = Invoice.objects.filter(warehouse=permission.warehouse)

    context = {
        'invoices': invoices,
        'warehouses': warehouses,
        'warehouse': warehouse
    }
    return render(request, 'invoice/invoices.html', context)

def create_invoice(request, warehouse_id):
    warehouse = Warehouse.objects.get(pk=warehouse_id)
    invoice = Invoice.objects.create(warehouse=warehouse)
    return redirect(reverse('invoice-create-form', kwargs={'invoice_id': invoice.id }))

def create_invoice_form(request, invoice_id):
    invoice = Invoice.objects.get(pk=invoice_id)
    products = Product.objects.filter(warehouse=invoice.warehouse)
    invoiceItems = InvoiceItem.objects.filter(invoice=invoice)
    form = InvoiceForm(instance=invoice)
    context = {
        'invoice': invoice,
        'form': form,
        'products': products,
        'invoiceitems': invoiceItems
    }
    return render(request, 'invoice/invoice_form.html', context)

def delete_invoice(request, pk):
    Invoice.objects.get(pk=pk).delete()
    return redirect(reverse('invoice-list'))

def varian_product_list(request, product_id):
    product = Product.objects.get(pk=product_id)
    varian_products = VarianProduct.objects.filter(product=product).values('varian_attribute', 'varian_value', 'stock', 'sell_price', 'id', 'product__name')
    data = {
        'varian_products': list(varian_products)
    }
    return JsonResponse(data)

def save_invoice_item(request, invoice_id):
    if request.method == "POST":
        form = InvoiceItemForm(request.POST)
        if form.is_valid():
            invoice = Invoice.objects.get(pk=invoice_id)
            varian = VarianProduct.objects.get(pk=form.cleaned_data['varian_product'].id)
            varian.stock = F('stock') - form.cleaned_data['quantity']
            varian.save()
            defaults = {
                'name': form.cleaned_data['name'],
                'sku': form.cleaned_data['sku'],
                'price': form.cleaned_data['price'],
                'quantity': form.cleaned_data['quantity'],
            }
            item, created = InvoiceItem.objects.update_or_create(invoice=invoice, varian_product=form.cleaned_data['varian_product'], defaults=defaults)

            data = { 'item': model_to_dict(item), 'created': created }
            return JsonResponse(data)
        else:
            return JsonResponse({'status': 'false', 'message': "Form isn't valid!" }, status=400)

def delete_invoice_item(request, pk):
    if request.method == 'POST':
        item = InvoiceItem.objects.get(pk=pk)
        varian = VarianProduct.objects.get(pk=item.varian_product.id)
        varian.stock = F('stock') + item.quantity
        varian.save()
        item.delete()
        data = {
            message: 'Item successfully deleted'
        }
        return JsonResponse(data)
