from django.shortcuts import render
from django.template import Template
from django.http import HttpResponse
from django.template.loader import get_template, render_to_string

# Create your views here.
from django.shortcuts import render
from mainapp.models import ProductCategory, Product

# НА ГЛАВНУЮ страницу выводит данные из БД, но мне нужно не на главную, а в каталог.
def main(request):
    title = 'главная'
    products = Product.objects.all()[:]
    content = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', content)
    # return render(request, 'mainapp/index.html')

def catalog(request):
    title = 'Каталог мобильных товаров'
    catalog = ProductCategory.objects.all()[:]
    content = {'title': title, 'catalog': catalog}
    return render(request, 'mainapp/pages/catalog.html', content)

def products(request):
    title = 'Каталог мобильных товаров'
    products = Product.objects.all()[:]
    content = {'title': title, 'products': products}
    return render(request, 'mainapp/pages/catalog.html', content)

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