from django.shortcuts import render,reverse
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('app2中的index方法')


def show(request, id):
    return HttpResponse('app2中的show方法，参数id值为' + str(id))


def show_uuid(request, id):
    return HttpResponse('app2中的show_uuid方法，参数id值为' + str(id))


def show_slug(request, q):
    return HttpResponse('app2中的show_slug方法，参数q值为' + str(q))


def article_list(request, year):
    return HttpResponse('app2中的article_list方法，参数year,指定4位值为' + str(year))


def article_page(request, page, key):
    return HttpResponse('app2中的article_list方法，参数page为数字值为' + str(page) + '参数key值为' + key)

"""反向解析路由"""
def url_reverse(request):
    #使用reverse()反向解析
    print('在views()函数中使用reverse()方法解析的结果：'+reverse('app2_url_reverse'))
    return render(request,'2/url_reverse.html')
