from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
"""控制器主要由views.py和urls.py组成"""


def index(request):
    return render(request, '1/index.html')

def index1(request):
    return HttpResponse('app1中的index1方法')
