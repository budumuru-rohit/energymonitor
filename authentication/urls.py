from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
     path("",views.home_view,name="home"),
     path('signup',views.signup,name="signup"),
     path('signout',views.signout,name="signout"), 
     path('dash',views.dash), 
     path("",include('app.urls')),

]