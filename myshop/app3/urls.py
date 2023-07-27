from django.contrib import admin
from django.urls import path, include, re_path
from app3 import views

urlpatterns = [
    path('app3/var/', views.var),
    path('app3/for_label/', views.for_label),
    path('app3/template_filter/', views.template_filter),
    path('app3/html_filter/', views.html_filter),
]
