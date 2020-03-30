from django.urls import path
from . import views

urlpatterns = [
    path('contacts/', views.contacts, name='account-contacts'),
    path('manage-accounts/', views.manage_accounts, name='account-manage-accounts')
]