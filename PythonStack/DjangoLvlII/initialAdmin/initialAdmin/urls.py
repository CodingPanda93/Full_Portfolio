"""initialAdmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# From inside your project's urls.py file
from django.conf.urls import url, include
from django.contrib import admin

# THIS SECTION IS NEW!
# ********************
from apps.awesomeApp.models import User as U, Fruit, Donut, Group

class UAdmin(admin.ModelAdmin):
    pass
admin.site.register(U, UAdmin)

class FruitAdmin(admin.ModelAdmin):
    pass
admin.site.register(Fruit, FruitAdmin)

class DonutAdmin(admin.ModelAdmin):
    pass
admin.site.register(Donut, DonutAdmin)

class GroupAdmin(admin.ModelAdmin):
    pass
admin.site.register(Group, GroupAdmin)
# ****************

urlpatterns = [
# Your app's urls is lined to the project
    url(r'^admin/',admin.site.urls),
    url(r'^awesomeApp/', include('apps.awesomeApp.urls')),
]
