from django.conf.urls import url
from . import views


app_name="books"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^show_book/(?P<id>\d+)$', views.show_book, name='show_book'),
    url(r'^show_user/(?P<id>\d+)$', views.show_user, name='show_user'),
    url(r'^new$', views.new, name='new'),
    url(r'^create_book/(?P<id>\d+)$', views.create_book, name='create_book'),
    url(r'^create_review/(?P<id>\d+)$', views.create_review, name='create_review'),
    url(r'^update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^destroy/(?P<id>\d+)$', views.destroy, name='destroy'),
]
