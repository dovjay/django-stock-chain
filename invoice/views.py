from django.urls import reverse
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.db.models import F
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from .models import Invoice, InvoiceItem
from .forms import InvoiceForm, InvoiceItemForm
from account.models import Warehouse, Contact, PermissionWarehouse
from inventory.models import VarianProduct, Product
from django.forms.models import model_to_dict
from weasyprint import HTML, CSS

# Create your views here.

@login_required
def invoices(request):
    if request.user.is_superuser:
        if request.GET.get('warehouse_id'):
            warehouse = Warehouse.objects.get(pk=request.GET.get('warehouse_id'))
            warehouses = Warehouse.objects.all()
            invoices = Invoice.objects.filter(warehouse=warehouse).order_by('-invoice_no')
        else:
            warehouses = Warehouse.objects.all()
            warehouse = warehouses[0]
            url = reverse('invoice-list')
            qs = f'warehouse_id={warehouse.id}'
            return redirect(f'{url}?{qs}')

    else:
        permission = PermissionWarehouse.objects.get(user=request.user)
        warehouse = Warehouse.objects.get(pk=permission.warehouse.pk)
        warehouses = warehouse
        invoices = Invoice.objects.filter(warehouse=permission.warehouse).order_by('-invoice_no')

    context = {
        'invoices': invoices,
        'warehouses': warehouses,
        'warehouse': warehouse
    }
    return render(request, 'invoice/invoices.html', context)

@login_required
def create_invoice(request, warehouse_id):
    warehouse = Warehouse.objects.get(pk=warehouse_id)
    invoice = Invoice.objects.create(warehouse=warehouse)
    return redirect(reverse('invoice-form', kwargs={'invoice_id': invoice.id }))

@login_required
def invoice_form(request, invoice_id):
    alert = ''
    if request.method == "POST":
        invoice = Invoice.objects.get(pk=invoice_id)
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            form.save()
            return redirect(reverse('invoice-list'))
        else:
            alert = str(form.errors)
    
    invoice = Invoice.objects.get(pk=invoice_id)
    products = Product.objects.filter(warehouse=invoice.warehouse)
    invoiceItems = InvoiceItem.objects.filter(invoice=invoice)
    customers = Contact.objects.filter(owner=invoice.warehouse.owner)
    form = InvoiceForm(instance=invoice)
    context = {
        'invoice': invoice,
        'form': form,
        'products': products,
        'invoiceitems': invoiceItems,
        'customers': customers,
        'alert': alert
    }
    return render(request, 'invoice/invoice_form.html', context)

@login_required
def delete_invoice(request, pk):
    Invoice.objects.get(pk=pk).delete()
    return redirect(reverse('invoice-list'))

@login_required
def varian_product_list(request, product_id):
    product = Product.objects.get(pk=product_id)
    varian_products = VarianProduct.objects.filter(product=product).values('varian_attribute', 'varian_value', 'stock', 'sell_price', 'id', 'product__name')
    data = {
        'varian_products': list(varian_products)
    }
    return JsonResponse(data)

@login_required
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

@login_required
def delete_invoice_item(request, pk):
    if request.method == 'POST':
        item = InvoiceItem.objects.get(pk=pk)
        varian = VarianProduct.objects.get(pk=item.varian_product.id)
        varian.stock = F('stock') + item.quantity
        varian.save()
        item.delete()
        data = {
            'message': 'Item successfully deleted'
        }
        return JsonResponse(data)

@login_required
def generate_invoice_pdf(request, pk):
    invoice = Invoice.objects.get(pk=pk)
    invoiceitems = InvoiceItem.objects.filter(invoice=invoice)
    warehouse = Warehouse.objects.get(pk=invoice.warehouse.id)

    subtotal = 0
    for item in invoiceitems:
        subtotal += item.get_subtotal()

    context = {
        'invoice': invoice,
        'invoiceitems': invoiceitems,
        'warehouse': warehouse,
        'subtotal': subtotal
    }

    # render template into pdf and send to user
    html_template = get_template('invoice/invoice_pdf.html')
    html = html_template.render(context).encode(encoding='UTF-8')
    pdf_file = HTML(string=html).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'filename="{invoice.invoice_no}.pdf"'
    return response

# remove this after the template done
def invoice_example(request, pk):
    invoice = Invoice.objects.get(pk=pk)
    invoiceitems = InvoiceItem.objects.filter(invoice=invoice)
    warehouse = Warehouse.objects.get(pk=invoice.warehouse.id)

    subtotal = 0
    for item in invoiceitems:
        subtotal += item.get_subtotal()

    context = {
        'invoice': invoice,
        'invoiceitems': invoiceitems,
        'warehouse': warehouse,
        'subtotal': subtotal
    }
    
    return render(request, 'invoice/invoice_pdf.html', context)
