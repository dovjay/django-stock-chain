from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def contacts(request):
    return render(request, 'account/contacts.html')

def manage_accounts(request):
    return render(request, 'account/accounts.html')