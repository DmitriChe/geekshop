from django.shortcuts import render
from django.template import Template
from django.http import HttpResponse
from django.template.loader import get_template, render_to_string

# Create your views here.
from django.shortcuts import render
from .models import ProductCategory, Product


# def main(request):
#     template = Template(
#         '''
#         'HELLO, {{ name }}!'

#         '''
#     )


# def main(request):
#     title = 'главная'
#     products = Product.objects.all()[:4]
#     content = {'title': title, 'products': products}
#     return render(request, 'mainapp/index.html', content)

def main(request):
    return render(request, 'mainapp/index.html')

def products(request):
    # return render(request, 'mainapp/pages/catalog.html')
    context = {
        'pagename' : 'каталог товаров',
        'products' : [
            {'href': 'bicycle', 'src': 'images/bicycle.jpg', 'info': 'велосипед'},
            {'href': 'car', 'src': 'images/car.jpg', 'info': 'автомобиль'},
            {'href': 'helicopter', 'src': 'images/helicopter.jpg', 'info': 'вертолёт'},
            {'href': 'airplane', 'src': 'images/airplane.jpg', 'info': 'самолёт'},
            {'href': 'bicycle', 'src': 'images/bicycle.jpg', 'info': 'велосипед'},
            {'href': 'car', 'src': 'images/car.jpg', 'info': 'автомобиль'},
            {'href': 'helicopter', 'src': 'images/helicopter.jpg', 'info': 'вертолёт'},
            {'href': 'airplane', 'src': 'images/airplane.jpg', 'info': 'самолёт'},
            {'href': 'bicycle', 'src': 'images/bicycle.jpg', 'info': 'велосипед'},
            {'href': 'car', 'src': 'images/car.jpg', 'info': 'автомобиль'},
            {'href': 'helicopter', 'src': 'images/helicopter.jpg', 'info': 'вертолёт'},
            {'href': 'airplane', 'src': 'images/airplane.jpg', 'info': 'самолёт'},
            {'href': 'helicopter', 'src': 'images/helicopter.jpg', 'info': 'вертолёт'},
            {'href': 'airplane', 'src': 'images/airplane.jpg', 'info': 'самолёт'},
        ]
    }
    response_string = render_to_string('mainapp/pages/catalog.html', context)
    return HttpResponse(response_string)

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