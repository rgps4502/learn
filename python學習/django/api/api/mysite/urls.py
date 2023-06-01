from django.contrib import admin
from django.urls import path
from mysite import views
urlpatterns = [
    path('home/',views.home_page)
]