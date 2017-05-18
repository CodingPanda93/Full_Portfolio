from django.conf.urls import url

from . import views

app_name="secrets"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^secrets/most_popular$', views.popular name='popular'),
    url(r'^secrets/like/(?P<id>\d+)$', views.like name='like')
    url(r'^secrets/create$', views.create name='create'),
    url(r'^secrets/destroy/(?P<id>\d+)$', views.destroy name='destroy'),
]
