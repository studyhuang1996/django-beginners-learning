'''
Author: xiaoying
Date: 2020-11-19 00:27:47
LastEditTime: 2020-11-24 22:41:14
LastEditors: huangjy
Description: In User Settings Edit
FilePath: /myproject/myproject/urls.py
'''
"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from boards import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^boards/(?P<pk>\d+)/new/$',views.new_topic,name="new_topic"),
    url(r'^boards/(?P<pk>\d+)/$',views.baord_topic,name="board_topic"),
    url(r'^admin/', admin.site.urls),
]

