from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.index, name="index"),
    url(r'add/new$', views.create, name="create"),
    url(r'add/$', views.add_book, name="add_book"),
    url(r'(?P<id>[\d]+)/reviews/(?P<review_id>[\d]+)/destroy/$', views.destroy_review, name="destroy_review"),
    url(r'(?P<id>[\d]+)/reviews/$', views.add_review, name="add_review"),
    url(r'(?P<id>[\d]+)/', views.show_book, name="show_book")
]
