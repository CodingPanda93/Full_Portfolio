from django.conf.urls import url
from . import views

app_name = 'courses'
urlpatterns = [
    url(r'^$', views.index name='index'),
    url(r'^add$', views.add name='add'),
    url(r'^confirm_remove/(?P<id>\d+)$', views.confirm_remove name="confirm_remove"),
    url(r'^destroy/(?P<id>\d+)$', views.destroy name="destroy"),
    url(r'^add_user$', views.add_user name="add_user")
]
