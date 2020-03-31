from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='inventory-dashboard'),
    path('products/', views.products, name='inventory-products'),
    path('invoices/', views.invoices, name='inventory-invoices'),
    path('varian-product/', views.varian_product, name='inventory-varian-product'),
    path('product-form/', views.product_form, name='inventory-product-form')
]