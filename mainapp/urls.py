from django.conf.urls import url
import mainapp.views as mainapp

app_name = 'catalog'

urlpatterns = [
    url(r'^$', mainapp.catalog, name='index'),
    url(r'^(?P<pk>\d+)/$', mainapp.catalog, name='catalog'),
]