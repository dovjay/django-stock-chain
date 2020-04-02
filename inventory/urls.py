from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='inventory-dashboard'),
    path('products/', views.products, name='inventory-products'),
    path('invoices/', views.invoices, name='inventory-invoices'),
    path('varian-product/', views.varian_product, name='inventory-varian-product'),
    path('product-form/', views.product_form, name='inventory-product-form'),
    path('categories/', views.categories, name='inventory-categories'),
    path('create-category/', views.CreateCategory.as_view(), name='inventory-create-category'),
    path('update-category/<pk>/', views.UpdateCategory.as_view(), name='inventory-update-category'),
    path('delete-category/<pk>/', views.DeleteCategory.as_view(), name='inventory-delete-category')
]