from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.create, name="create"),
    url(r'^login/$', views.login, name="login"),
    url(r'^users/(?P<id>[\d]+)/$', views.user_reviews, name='user_reviews'),
    url(r'^logout/$', views.logout, name="logout")
]
