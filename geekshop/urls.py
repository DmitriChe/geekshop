"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path

from django.contrib import admin
import mainapp.views as mainapp

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', mainapp.main, name='main'),
    url(r'^catalog/', mainapp.catalog, name='catalog'),
    url(r'^products/', mainapp.products, name='products'),
    # url( r'^products/' , include( 'mainapp.urls' , namespace='products')),
    url(r'^contacts/', mainapp.contacts, name='contacts'),
    url(r'^bicycles/', mainapp.bicycles, name='bicycles'),
    url(r'^bicycle/', mainapp.bicycle, name='bicycle'),
    url(r'^cars/', mainapp.cars, name='cars'),
    url(r'^car/', mainapp.car, name='car'),
    url(r'^helicopters/', mainapp.helicopters, name='helicopters'),
    url(r'^helicopter/', mainapp.helicopter, name='helicopter'),
    url(r'^airplanes/', mainapp.airplanes, name='airplanes'),
    url(r'^airplane/', mainapp.airplane, name='airplane'),
    path('admin/', admin.site.urls),
]

# делаем папку MEDIA_ROOT доступной по сетевому адресу MEDIA_URL
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)