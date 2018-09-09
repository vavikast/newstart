from django.shortcuts import render
from django.http import  HttpResponse

from .forms import AddForm

def index(request):
    if request.method== 'POST' : #当提交工单时
        form =AddForm(request.POST)

        if form.is_valid(): #如果提交的数据合法
            a=form.cleaned_data['a']
            b=form.cleaned_data['b']
            return  HttpResponse(str(int(a)+int(b)))

    else: #当正常访问时
        form =AddForm()
    return  render(request,'blog/index.html',{'form':form})



