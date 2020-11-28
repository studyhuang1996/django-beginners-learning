'''
Author: your name
Date: 2020-11-19 00:35:48
LastEditTime: 2020-11-24 22:48:51
LastEditors: huangjy
Description: Test 用例
FilePath: /myproject/boards/tests.py
'''
from django.urls import reverse
from django.urls import resolve
from django.test import TestCase
from .views import baord_topic,new_topic,home
from .models import Board
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

class BoardTopicTests(TestCase):
    def setUp(self):
        Board.objects.create(name="Django",description='Django board')
    
    def test_board_topics_view_success_status_code(self):
        url = reverse('board_topic',kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code,200)
   
        
    def test_board_topics_view_not_found_code(self):
        url = reverse('board_topic',kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code,404)
        
    def test_board_topics_url_resolves_board_topics_view(self):
        '''
        description: 测试 Django 是否使用了正确的视图函数去渲染 topics。
        param {*}
        return {*}
        '''
        view = resolve('/boards/1/')
        self.assertEquals(view.func, baord_topic)
        
    def test_board_topics_view_contains_link_back_to_homepage(self):
        board_topics_url = reverse('board_topic', kwargs={'pk': 1})
        response = self.client.get(board_topics_url)
        homepage_url = reverse('home')
        self.assertContains(response, 'href="{0}"'.format(homepage_url))
        
class NewTopicTests(TestCase):
    def setUp(self):
        Board.objects.create(name='Django', description='Django board.')

    def test_new_topic_view_success_status_code(self):
        url = reverse('new_topic', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_new_topic_view_not_found_status_code(self):
        url = reverse('new_topic', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_new_topic_url_resolves_new_topic_view(self):
        view = resolve('/boards/1/new/')
        self.assertEquals(view.func, new_topic)

    def test_new_topic_view_contains_link_back_to_board_topics_view(self):
        new_topic_url = reverse('new_topic', kwargs={'pk': 1})
        board_topics_url = reverse('board_topic', kwargs={'pk': 1})
        response = self.client.get(new_topic_url)