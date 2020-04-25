from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.invoices, name='invoice-list'),
    path('create-invoice/<int:warehouse_id>/', views.create_invoice, name='invoice-create'),
    path('invoice-form/<int:invoice_id>/', views.invoice_form, name='invoice-form'),
    path('delete-invoice/<int:pk>/', views.delete_invoice, name='invoice-delete'),
    path('varian-product/<int:product_id>/', views.varian_product_list, name='invoice-varian-product-list'),
    path('save-invoice-item/<int:invoice_id>/', views.save_invoice_item, name='invoice-save-invoice-item'),
    path('delete-invoice-item/<int:pk>/', views.delete_invoice_item, name='invoice-delete-invoice-item'),
    path('generate-pdf/<int:pk>/', views.generate_invoice_pdf, name='invoice-generate-pdf'),
    # delete this after template view suffice
    path('invoice-example/<int:pk>/', views.invoice_example, name="invoice-example")
]