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


# ВАРИАНТ 1 - работает, хотя указан неверный шаблон mainapp/index.html
# def products(request):
#     title = 'главная'
#     products = Product.objects.all()[:]
#     content = {'title': title, 'products': products}
#     return render(request, 'mainapp/index.html', content)

# ВАРИАНТ 2 - не работает, хотя я указываю тот шаблон, куда мне нужно выводить данные mainapp/pages/catalog.html
def products(request):
    title = 'главная'
    products = Product.objects.all()[:]
    content = {'title': title, 'products': products}
    return render(request, 'mainapp/pages/catalog.html', content)

# ВАРИАНТ 3 - так тоже не работает... - не знаю почему
# def products(request):
#     title = 'главная'
#     products = Product.objects.all()[:]
#     content = {'title': title, 'products': products}
#     response_string = render_to_string('mainapp/pages/catalog.html', content)
#     return HttpResponse(response_string)


# ВАРИАНТ 4 - а так работает, понятно почему
# def products(request):
#     ## return render(request, 'mainapp/pages/catalog.html')

#     context = {
#         'pagename' : 'каталог товаров',
#         'products' : [
#             {'href': 'bicycle', 'src': 'images/bicycle.jpg', 'info': 'велосипед'},
#             {'href': 'car', 'src': 'images/car.jpg', 'info': 'автомобиль'},
#             {'href': 'helicopter', 'src': 'images/helicopter.jpg', 'info': 'вертолёт'},
#             {'href': 'airplane', 'src': 'images/airplane.jpg', 'info': 'самолёт'},
#             {'href': 'bicycle', 'src': 'images/bicycle.jpg', 'info': 'велосипед'},
#             {'href': 'car', 'src': 'images/car.jpg', 'info': 'автомобиль'},
#             {'href': 'helicopter', 'src': 'images/helicopter.jpg', 'info': 'вертолёт'},
#             {'href': 'airplane', 'src': 'images/airplane.jpg', 'info': 'самолёт'},
#             {'href': 'bicycle', 'src': 'images/bicycle.jpg', 'info': 'велосипед'},
#             {'href': 'car', 'src': 'images/car.jpg', 'info': 'автомобиль'},
#             {'href': 'helicopter', 'src': 'images/helicopter.jpg', 'info': 'вертолёт'},
#             {'href': 'airplane', 'src': 'images/airplane.jpg', 'info': 'самолёт'},
#             {'href': 'helicopter', 'src': 'images/helicopter.jpg', 'info': 'вертолёт'},
#             {'href': 'airplane', 'src': 'images/airplane.jpg', 'info': 'самолёт'},
#         ]
#     }
#     response_string = render_to_string('mainapp/pages/catalog.html', context)
#     return HttpResponse(response_string)

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