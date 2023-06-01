from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home_page(request):
    return render(request,"mysite/home.html",{"result":"abc.com","name":'jea'})