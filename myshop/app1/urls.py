from django.contrib import admin
from django.urls import path, include
from app1 import views

urlpatterns = [
    path('app1/index/', views.index1),  # 定义了路由index/ 以及该路由指向的视图函数index()
]
