from django.shortcuts import render
from django.template import Template
from django.http import HttpResponse
from django.template.loader import get_template, render_to_string
from django.shortcuts import render
from mainapp.models import ProductCategory, Product
from django.shortcuts import get_object_or_404


# Create your views here.
# НА ГЛАВНУЮ страницу выводит данные из БД, но мне нужно не на главную, а в каталог.
def main(request):
    return render(request, 'mainapp/index.html')


def catalog(request, pk=None):
    print(pk)

    title = 'Каталог мобильных товаров'
    # Импортируем из модель ProductCategory все категории в links_menu
    links_menu = ProductCategory.objects.all()
    # catalog = ProductCategory.objects.all()[:]

    if pk:
        if pk == '0':
            category = {'name': 'все'}
            message = 'pk = 0'
            # получаем в переменную products из модели Product все товары
            products = Product.objects.all().order_by('price')
        else:
            message = 'pk != 0'
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')
        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
            'message': message,
        }
        return render(request, 'mainapp/pages/products_list.html', content)


    same_products = Product.objects.all()[3: 5]
    # Добавил, чтобы выводились товары даже когда не указана категория
    products = Product.objects.all().order_by('price')
    message = 'не указан номер категории!'
    content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products,
        'message': message,
        # Добавил, чтобы выводились товары даже когда не указана категория
        'products': products
    }
    return render(request, 'mainapp/pages/catalog.html', content)


# def catalog(request, pk=None):
#     print(pk)
#
#     title = 'Каталог мобильных товаров'
#     catalog = ProductCategory.objects.all()[:]
#     content = {'title': title, 'catalog': catalog}
#     return render(request, 'mainapp/pages/catalog.html', content)

# def products(request):
#     title = 'Каталог мобильных товаров'
#     products = Product.objects.all()[:]
#     content = {'title': title, 'products': products}
#     return render(request, 'mainapp/pages/catalog.html', content)


def contacts(request):
    return render(request, 'mainapp/pages/contacts.html')


def bicycles(request):
    return render(request, 'mainapp/pages/bicycle.html')


def cars(request):
    return render(request, 'mainapp/pages/car.html')


def helicopters(request):
    return render(request, 'mainapp/pages/helicopter.html')


def airplanes(request):
    return render(request, 'mainapp/pages/airplane.html')


def bicycle(request):
    return render(request, 'mainapp/pages/bicycle.html')


def car(request):
    return render(request, 'mainapp/pages/car.html')


def helicopter(request):
    return render(request, 'mainapp/pages/helicopter.html')


def airplane(request):
    return render(request, 'mainapp/pages/airplane.html')
