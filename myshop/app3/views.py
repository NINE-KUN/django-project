from django.shortcuts import render
from django.http import HttpResponse
import datetime


def var(request):
    """模板变量"""
    """模板变量可以是字符串，列表，字典和类对象"""
    # v=PersonInfo.objects.all()
    # print(v)
    # 列表对象
    lists = ['Java', 'Python', 'C', 'C#', 'JavaScript']
    # 字典对象
    dicts = {'姓名': '钱坤', '年龄': 25, '性别': '男'}

    return render(request, '3/var.html', {'lists': lists, 'dicts': dicts})


def for_label(request):
    """模板标签
       先创建模板变量 然后将变量传递给模板
       模板通过模板标签对数据进行处理"""
    dict1 = {'书名': 'Django开发', '价格': 80, '作者': '张三'}
    dict2 = {'书名': 'Python开发', '价格': 90, '作者': '李四'}
    dict3 = {'书名': 'Java开发', '价格': 100, '作者': '王五'}
    lists = [dict1, dict2, dict3]
    return render(request, '3/for_label.html', {'lists': lists})


def template_filter(request):
    """模板过滤器
       模板过滤器用于对模板变量进行操作
       模板过滤器的语法格式
       {{ 变量名 | 过滤器： 参数}}
       """
    # 定义网址
    # url_addr="<table border=1><tr><td>这是一个表格</td></tr></table>";
    str1 = "abcdefg"
    str2 = "ABCDEFG"
    slice_str = "1234567890"
    time_str = datetime.datetime.now()
    return render(request, '3/template_filter.html',
                  {"str1": str1, "str2": str2, "slice_str": slice_str, "time_str": time_str})


"""模板高级用法
   模板转义：django会对HTML标签和JavaScript标签进行转义，以提高代码安全
   如将JavaScript"<"转义为"&it，将","转义为"&#39
   可以通过 模板变量|safe 的方式来告诉django这段代码是安全的，不需要转义"""""


def html_filter(request):
    html_addr = "<table border=1><tr><td>这是一个表格</td></tr></table>"
    html_script = "<script language='javascript'>document.write('非法执行');</script>"
    return render(request, '3/html_filter.html', {"html_addr": html_addr, "html_script": html_script})
