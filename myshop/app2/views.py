from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from .models import *


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
    # 使用reverse()反向解析
    print('在views()函数中使用reverse()方法解析的结果：' + reverse('app2_url_reverse'))
    return render(request, '2/url_reverse.html')


"""HttpRequest用法"""


def test_get(request):
    print(request.get_host())  # 域名+端口
    print(request.get_raw_uri())  # 全部路径，包含参数
    print(request.path)  # 获取访问文件路径，不含参数
    print(request.get_full_path())  # 获取访问文件路径，包含参数
    print(request.method)  # 获取请求中的使用的HTTP方式(POST/GET)
    print(request.GET)  # 获取GET请求的参数
    print(request.META["HTTP_USER_AGENT"])  # 用户浏览器的user-agent字符串
    print(request.META["REMOTE_ADDR"])  # 客户端IP
    print(request.GET.get('username'))  # 获取get参数
    return HttpResponse("")


def test_post(request):
    print(request.method)  # 获取请求中的使用的HTTP方式(POST/GET)
    print(request.POST.get('username'))
    return render(request, '2/test_post.html')


def test_render(request):
    """render()函数，根据模板文件和传递给模板文件的字典类型的变量，
        生成一个HttpResponse对象返回
        将info的值'hello django' 传给html中的info"""
    return render(request, '2/test_render.html', {'info': 'hello django'}, content_type='text/html')


"""在Django中，使用重定向函数redirect()实现网页重定向，该函数包含3种情况
    1.通过调用模型get_absolute_url()函数进行重定向
    2.通过路由反向解析进行重定向
    3.通过一个绝对的或相对的URL，让浏览器跳转到指定的URL进行重定向"""


def test_redirect(request):
    """通过一个绝对的或相对的URL，让浏览器跳转到指定的URL进行重定向"""
    return redirect("https://www.baidu.com/")


def test_redirect_model(request, id):
    """通过调用模型中get_absolute_url()函数进行重定向"""
    """通过url定位到该视图函数，函数redirect()中包含一个模型实例
        因此会调用该模型实例的get_absolute_url()方法，而get_absolute_url()方法中
        通过reverse()函数做反向解析，组装出app2/userinfo/<int:id>/重定向"""
    user = UserBaseInfo.objects.get(id=id)
    return redirect(user)


def userinfo(request, id):
    user = UserBaseInfo.objects.get(id=id)
    return HttpResponse("编号：" + str(user.id) + " 姓名：" + user.username)
