from django.conf.urls import url
from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns =[

    path('',views.register,name='register'),
    path('index',views.index,name='index'),


]