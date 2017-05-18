from django.conf.urls import url
from . import views

urlpatterns = [
	url(r"^$", views.index, name="index"),
	url(r'^sports2$', views.sport_orm2, name="sports2"),
	url(r"^make_data/", views.make_data, name="make_data"),
]
