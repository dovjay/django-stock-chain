from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def settings(request):
    return HttpResponse("Nice catch!")