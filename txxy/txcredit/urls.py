#-*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path
from txcredit import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('home/', views.home, name='home'),
    path('home1/', views.home1, name='home1'),
    path('home/add/', views.add, name='add'),
    path('add/<int:a>/<int:b>/', views.add2, name='add2'),

]
