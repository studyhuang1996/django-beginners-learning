'''
Author: your name
Date: 2020-11-19 00:35:48
LastEditTime: 2020-11-22 19:11:21
LastEditors: huangjy
Description: 视图
FilePath: /myproject/boards/views.py
'''
from django.shortcuts import render
from django.http import HttpResponse
from .models import Board
# Create your views here.


#def home(request):
 #   return HttpResponse('Hello, World!')

'''
description: b板块列表页
param {*}
return {*}
'''
# def home(request):
#     boards = Board.objects.all()
#     boards_names = list()
#     for board in boards:
#         boards_names.append(board)
#     response_html = '<br>'.join('%s' %id for id in boards_names)
#     return HttpResponse(response_html)

def home(request):
    """
    定义首页页面
    """
    boards = Board.objects.all()
    return render(request,"home.html",{'boards':boards})

def baord_topic(request,pk):
    board = Board.objects.get(pk=pk)
    return render(request,"topic.html",{'board':board})