from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("base",views.base,name="base"),
    path("power",views.power,name="power"),
    path("oee",views.oee,name='oee'),
    path("test",views.data_view,name='test'),
    path("home",views.home,name="home")
]