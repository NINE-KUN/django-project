from django.views import View
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from .models import *

"""等同于
def index_page(request):
    if request.method == 'GET':
        return HttpResponse("get请求")
    elif request.method == 'POST':
        return HttpResponse("post请求")
"""


class IndexPageView(View):
    '''
    类视图 采用了面向对象的思想
    视图类继承django.views下的View类
    '''

    def get(self, request):
        return HttpResponse("get请求")

    def post(self, request):
        return HttpResponse("post请求")


class TestTemplateView(TemplateView):
    """通用视图类"""
    # 设置模板文件
    template_name = "2/test_template_view.html"

    # 重写父类get_context_data()方法,获取新增的额外变量
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 在context字段中加入新增的变量info，就可以通过模板中的{{info}}得到传递的字典变量
        context["info"] = "该变量可以传递到模板"
        return context


class TestListView(ListView):
    """别表视图类---ListView"""
    # 设置模型
    model = UserBaseInfo
    # 设置模板文件
    template_name = "2/test_listview.html"
    # 设置模板变量
    context_object_name = "users"
    # 每页显示的条数
    paginate_by = 1

    # queryset=UserBaseInfo.objects.filter(status=1)
    # 重写父类的get_queryset()方法获取属性queryset的值
    def get_queryset(self):
        # 返回状态为1的数据
        userinfo = UserBaseInfo.objects.all()
        return userinfo

    # 重写父类get_context_data()方法来获取新增的额外变量
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 增加模板变量info
        context["info"] = "ListView变量可以传递到模板"
        print(context)
        return context


class TestDetailView(DetailView):
    """详细视图类---DetailView"""
    # 设置模型
    model = UserBaseInfo
    # 设置模板文件
    template_name = "2/test_detailview.html"
    # 设置模板变量
    context_object_name = "users"
    # 代表路由地址中某个参数，该参数用于保存记录得主键字段值
    pk_url_kwarg = 'userid'
