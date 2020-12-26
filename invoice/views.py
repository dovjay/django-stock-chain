from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.db.models import F, Q
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from .models import Invoice, InvoiceItem
from .forms import InvoiceForm, InvoiceItemForm
from account.models import Warehouse, Contact, PermissionWarehouse
from inventory.models import VarianProduct, Product
from django.forms.models import model_to_dict
from weasyprint import HTML, CSS
import csv

# Create your views here.

@login_required
def invoices(request):
    if request.user.is_superuser:
        if request.GET.get('warehouse_id'):
            warehouse = Warehouse.objects.get(pk=request.GET.get('warehouse_id'))
            warehouses = Warehouse.objects.all()
            invoices = Invoice.objects.filter(warehouse=warehouse)

            # search
            if request.GET.get('q'):
                query = request.GET.get('q')
                invoices = Invoice.objects.filter(Q(warehouse=warehouse), Q(customer__contains=query) | Q(invoice_no__contains=query)).order_by('-invoice_no')
            else:
                invoices = Invoice.objects.filter(warehouse=warehouse).order_by('-invoice_no')

        else:
            warehouses = Warehouse.objects.all()
            if warehouses:
                warehouse = warehouses[0]
            else:
                return redirect(reverse('account-create-warehouse'))
            url = reverse('invoice-list')
            qs = f'warehouse_id={warehouse.id}'
            return redirect(f'{url}?{qs}')

    else:
        try:
            permission = PermissionWarehouse.objects.get(user=request.user)
        except ObjectDoesNotExist:
            return HttpResponse("403 Forbidden: Coba minta akses ke admin untuk mengakses data")
        warehouse = Warehouse.objects.get(pk=permission.warehouse.pk)
        warehouses = warehouse

        # search
        if request.GET.get('q'):
            query = request.GET.get('q')
            invoices = Invoice.objects.filter(Q(warehouse=permission.warehouse), Q(customer__contains=query) | Q(invoice_no__contains=query)).order_by('-invoice_no')
        else:
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
    varian_products = VarianProduct.objects.filter(product=product).values('size', 'stock', 'sell_price', 'id', 'product__name', 'product__image')
    data = {
        'varian_products': list(varian_products)
    }
    return JsonResponse(data)

@login_required
def get_invoice_items(request, invoice_id):
    invoice = Invoice.objects.get(pk=invoice_id)
    items = InvoiceItem.objects.filter(invoice=invoice).values('varian_product__product__image', 'varian_product__size', 'sku', 'price', 'quantity', 'name')
    data = {
        'invoice_no': invoice.invoice_no,
        'items': list(items)
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

@login_required
def export_invoices_to_csv(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = "attachment;filename=invoice_list.csv"

    field_names = ["No", "Customer", "Status", "Due", "Paid Date", "Subtotal", "Discount", "Total" "Created", "Updated"]

    writer = csv.writer(response)
    writer.writerow(field_names)

    warehouse = Warehouse.objects.get(pk=request.COOKIES.get('warehouse_id'))
    invoices = Invoice.objects.filter(Q(warehouse=warehouse), ~Q(status="DRAFT"))

    for invoice in invoices:
        row = [invoice.invoice_no, invoice.customer, invoice.status, invoice.due, invoice.paid_date, invoice.total, f'{invoice.discount}%', invoice.get_total(), invoice.created, invoice.updated]
        writer.writerow(row)

    return response