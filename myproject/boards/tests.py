'''
Author: your name
Date: 2020-11-19 00:35:48
LastEditTime: 2020-11-22 11:35:21
LastEditors: huangjy
Description: Test 用例
FilePath: /myproject/boards/tests.py
'''
from django.urls import reverse
from django.urls import resolve
from django.test import TestCase
from .views import home

# Create your tests here.

class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code,200)
    
    def test_home_url_resolves_home_view(self):
        '''
        description: resolve Django使用它来将浏览器发起请求的URL与urls.py模块中列出的URL进行匹配。
        该测试用于确定URL / 返回 home 视图。
        param {*} self
        return {*}
        '''  
        view = resolve('/')
        self.assertEquals(view.func,home)   
   