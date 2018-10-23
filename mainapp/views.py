from django.shortcuts import render
from django.template import Template
from django.http import HttpResponse
from django.template.loader import get_template

# Create your views here.
from django.shortcuts import render

def main(request):
    return render(request, 'mainapp/index.html')

def products(request):
    return render(request, 'mainapp/pages/catalog.html')

def contacts(request):
    return render(request, 'mainapp/pages/contacts.html')

def bicycle(request):
    return render(request, 'mainapp/pages/bicycle.html')

def car(request):
    return render(request, 'mainapp/pages/car.html')

def helicopter(request):
    return render(request, 'mainapp/pages/helicopter.html')
    
def airplane(request):
    return render(request, 'mainapp/pages/airplane.html')