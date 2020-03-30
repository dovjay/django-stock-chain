from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='inventory-dashboard'),
    path('products/', views.products, name='inventory-products'),
    path('invoices/', views.invoices, name='inventory-invoices')
]