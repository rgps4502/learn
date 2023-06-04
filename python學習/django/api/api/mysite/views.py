from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

def home_page(request):
    post = models.fourm_post.objects.get(pk=3)
    return render(request,"mysite/home.html",{"post":post})