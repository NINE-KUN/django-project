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


"""反向解析路由reverse()"""

"""先根据路由app2/url_reverse/ 定位到该路由下的函数url_reverse()
   该函数反向解析了路由 所以通过路由名称为app2_url_reverse1 找到该路由app2/url_reverse1/下的视图函数
   url_reverse1()该视图函数使用了render()通过该函数调用了模板
   模板中{% url 'app2_url_reverse' %}将定位到name=app2_url_reverse的路由中的函数"""
"""
http://127.0.0.1:8000/app2/url_reverse/ 会因为重定向访问到'在views()函数中使用reverse()方法解析的结果：' + reverse('app2_url_reverse1'))
http://127.0.0.1:8000/app2/url_reverse1/ 因为没有重定向只会访问到模板  在HTML中使用url标签进行反向解析 app2_url_reverse
"""


def url_reverse(request):
    # 使用reverse()反向解析
    return HttpResponse('在views()函数中使用reverse()方法解析的结果：' + reverse('app2_url_reverse1'))


def url_reverse1(request):
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

"""通过一个绝对的或相对的URL，让浏览器跳转到指定的URL进行重定向"""


def test_redirect(request):
    """通过一个绝对的或相对的URL，让浏览器跳转到指定的URL进行重定向"""
    return redirect("https://www.baidu.com/")


def test_redirect_model(request, id):
    """通过调用模型中get_absolute_url()函数进行重定向"""
    """通过url定位到该视图函数test_redirect_model()，函数redirect()中包含一个模型实例
       因此会调用该模型实例的get_absolute_url()方法，而get_absolute_url()方法中
       通过reverse()函数，去找url中name为app2_userinfo做反向解析，组装出app2/userinfo/<int:id>/路由规则，
       然后根据该规则，找到对应的视图函数userinfo()"""
    user = UserBaseInfo.objects.get(id=id)
    return redirect(user)


def userinfo(request, id):
    user = UserBaseInfo.objects.get(id=id)
    return HttpResponse("编号：" + str(user.id) + " 姓名：" + user.username)


"""通过路由反向解析进行重定向"""


def test_redirect_views(request, id):
    """redirect()直接反向解析路由和使用reverse()一样 找到name为app2_userinfo的路由
       然后通过该路由下的视图方法userinfo()以达到重定向"""
    return redirect('app2_userinfo', id)


