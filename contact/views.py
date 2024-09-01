from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def contact(request):
    return HttpResponse('<h1>Tu jest kontakt</h1>')
