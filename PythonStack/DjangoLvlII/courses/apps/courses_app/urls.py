from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add),
    url(r'^confirm_remove/(?P<id>\d+)$', views.confirm_remove),
    url(r'^destroy/(?P<id>\d+)$', views.destroy),
]
