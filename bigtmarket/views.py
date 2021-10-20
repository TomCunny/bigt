from django.http.response import HttpResponse, HttpResponseGone
from django.shortcuts import render
from django.http import request
from bigt.templates import *

# Create your views here.
def contact(request):
    return render(request, template_name='contact.html')

def products(request):
    return render(request, template_name='product.html')

def index_home(request):
    return render(request, template_name='index.html')

def login_register(request):
    return render(request, template_name='logreg.html')

def order(request):
    return render(request, 'orderform.html')