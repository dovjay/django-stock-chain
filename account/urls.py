from django.urls import path
from . import views

urlpatterns = [
    path('contacts/', views.contacts, name='account-contacts'),
    path('create-contact/', views.CreateContact.as_view(), name="account-create-contact"),
    path('update-contact/<int:pk>/', views.UpdateContact.as_view(), name="account-update-contact"),
    path('delete-contact/<int:pk>/', views.DeleteContact.as_view(), name="account-delete-contact"),
    path('manage-accounts/', views.manage_accounts, name='account-manage-accounts')
]