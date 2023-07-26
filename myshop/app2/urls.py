from django.contrib import admin
from django.urls import path, include, re_path
from app2 import views

urlpatterns = [
    path('app2/index/', views.index),  # 定义了路由index/ 以及该路由指向的视图函数index()
    path('show/<int:id>/', views.show),  # url参数动态配置 <参数数据类型：参数名称>

    # 匹配uuid格式的字符串，该对象必须包含- http://127.0.0.1:8000/app2/article/00000-00000-0000-0000-00000/
    path('app2/article/<uuid:id>/', views.show_uuid, name='show_uuid'),

    # 匹配任何ASCII字符、连接符、下划线http://127.0.0.1:8000/app2/article/abc123/
    path('app2/article/<slug:q>/', views.show_slug, name='show_slug'),

    # re_path() 编写url时可以用正则表达式 (?P<name>pattern)name是匹配的字符串名称 pattern是要匹配的模式
    re_path('app2/list/(?P<year>\d{4})/', views.article_list),  # 后面跟4位整数的路由() http://127.0.0.1:8000/app2/list/2023/

    # 后面跟任意位整数路由且第2个参数可以是字母、数字、下划线http://127.0.0.1:8000/app2/list/1&key=a/
    re_path('app2/list/(?P<page>\d+)&key=(?P<key>\w+)/', views.article_page, name='article_page'),

    # 反向解析路由
    path('app2/url_reverse/', views.url_reverse, name='app2_url_reverse'),

    # HttpRequest用法
    path('app2/test_get/', views.test_get),

    # 获取post传递的值
    path('app2/test_post/', views.test_post),

    # render()函数，根据模板文件和传递给模板文件的字典类型的变量，生成一个HttpResponse对象返回
    path('app2/test_render/', views.test_render, name='app2_test_render'),

    # 通过一个绝对的或相对的URL，让浏览器跳转到指定的URL进行重定向
    path('app2/test_redirect/', views.test_redirect, name='app2_test_redirect'),

    # 通过定义get_absolute_url()方法 返回模型对外的url；使用reverse()函数做反向解析操作
    path('app2/test_redirect_model/<int:id>/', views.test_redirect_model, name='app2_test_redirect_model'),
    path('app2/userinfo/<int:id>/', views.userinfo, name='app2_userinfo'),

]
