from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='inventory-dashboard'),
    path('varian-product/', views.varian_product, name='inventory-varian-product'),
    path('create-varian-product/<int:project_id>/', views.CreateVarianProduct.as_view(), name='inventory-create-varian-product'),
    path('update-varian-product/<int:pk>/', views.UpdateVarianProduct.as_view(), name='inventory-update-varian-product'),
    path('delete-varian-product/<int:pk>/', views.DeleteVarianProduct.as_view(), name='inventory-delete-varian-product'),
    path('products/', views.products, name='inventory-products'),
    path('create-product/', views.CreateProduct.as_view(), name='inventory-create-product'),
    path('update-product/<int:pk>/', views.UpdateProduct.as_view(), name='inventory-update-product'),
    path('delete-product/<int:pk>/', views.DeleteProduct.as_view(), name='inventory-delete-product'),
    path('categories/', views.categories, name='inventory-categories'),
    path('create-category/', views.CreateCategory.as_view(), name='inventory-create-category'),
    path('update-category/<int:pk>/', views.UpdateCategory.as_view(), name='inventory-update-category'),
    path('delete-category/<int:pk>/', views.DeleteCategory.as_view(), name='inventory-delete-category')
]