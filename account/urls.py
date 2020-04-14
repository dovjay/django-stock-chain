from django.urls import path
from . import views

urlpatterns = [
    path('contacts/', views.contacts, name='account-contacts'),
    path('create-contact/', views.CreateContact.as_view(), name="account-create-contact"),
    path('update-contact/<int:pk>/', views.UpdateContact.as_view(), name="account-update-contact"),
    path('delete-contact/<int:pk>/', views.DeleteContact.as_view(), name="account-delete-contact"),
    path('manage-accounts/', views.manage_accounts, name='account-manage-accounts'),
    path('create-warehouse/', views.CreateWarehouse.as_view(), name="account-create-warehouse"),
    path('update-warehouse/<int:pk>/', views.UpdateWarehouse.as_view(), name="account-update-warehouse"),
    path('delete-warehouse/<int:pk>/', views.DeleteWarehouse.as_view(), name="account-delete-warehouse"),
    path('create-permission/', views.CreatePermissionWarehouse.as_view(), name="account-create-permission"),
    path('delete-permission/<int:pk>/', views.DeletePermissionWarehouse.as_view(), name="account-delete-permission"),
    path('create-account/', views.CreateAccount.as_view(), name="account-create-account"),
    path('update-account/<int:pk>/', views.UpdateAccount.as_view(), name="account-update-account"),
    path('delete-account/<int:pk>/', views.DeleteAccount.as_view(), name="account-delete-account"),
]