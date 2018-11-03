from django.conf.urls import url
import mainapp.views as mainapp

app_name = 'catalog'

urlpatterns = [
    url(r'^$', mainapp.products_list, name='index'),
    url(r'^(?P<pk>\d+)/$', mainapp.products_list, name='catalog'),
]