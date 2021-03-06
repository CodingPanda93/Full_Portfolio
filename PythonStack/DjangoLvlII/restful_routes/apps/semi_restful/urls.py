from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^products$', views.index, name='index'),
    url(r'^products/(?P<id>\d+)/show$', views.show, name='show'),
    url(r'^products/new$', views.new, name='new'),
    url(r'^products/(?P<id>\d+)/edit$', views.edit, name='edit'),
    url(r'^products/create$', views.create, name='create'),
    url(r'^products/(?P<id>\d+)/update$', views.update, name='update'),
    url(r'^products/(?P<id>\d+)/destroy$', views.destroy, name='destroy'),
]
