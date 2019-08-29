from django.urls import path

# app(directory)의 views.py
from . import views

urlpatterns = [
    path('push/', views.push),
    path('pull/', views.pull),
]