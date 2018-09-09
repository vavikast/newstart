#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import  HttpResponse

def home(request):
    return render(request,'home.html')

def home1(request):
    return render(render,'home1.html',request.path)
    #List = map(str, range(100))# 一个长度为100的 List
    #return render(request, 'home1.html', {'List': List})

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return HttpResponse(str(a+b))

def index(request):
    return HttpResponse("欢迎来到天下信用")

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))

def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))
