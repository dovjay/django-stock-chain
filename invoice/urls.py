from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.invoices, name='invoice-list'),
    path('create-invoice/<int:warehouse_id>/', views.create_invoice, name='invoice-create'),
    path('create-invoice-form/<int:invoice_id>/', views.create_invoice_form, name='invoice-create-form'),
    path('delete-invoice/<int:pk>/', views.delete_invoice, name='invoice-delete'),
    path('varian-product/<int:product_id>/', views.varian_product_list, name='invoice-varian-product-list'),
    path('save-invoice-item/<int:invoice_id>/', views.save_invoice_item, name='invoice-save-invoice-item'),
    path('delete-invoice-item/<int:pk>/', views.delete_invoice_item, name='invoice-delete-invoice-item'),
]