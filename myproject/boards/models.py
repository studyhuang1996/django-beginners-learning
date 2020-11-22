'''
Author: huangjy
Date: 2020-11-19 00:35:48
LastEditTime: 2020-11-22 10:35:17
LastEditors: huangjy
Description: 模型，创建数据库对象
FilePath: /myproject/boards/models.py
'''
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

'''
description:  创建数据库表的实体，这些信息将用于创建数据库列
param {*}
return {*}
'''
class Board(models.Model):
    #唯一值
    name = models.CharField(max_length=30,unique=True)
    description = models.CharField(max_length=100) 
    def __str__(self):
        #return  self.id,self.name,self.description
        return "板块id：%d, 板块名称：%s,描述：%s" %(self.id,self.name,self.description)  
    
class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board,related_name="topics",on_delete=models.CASCADE)
    starter = models.ForeignKey(User,related_name="topics",on_delete=models.CASCADE)


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic,related_name='posts',on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add= True)
    update_at = models.DateTimeField(null=True)
    create_by =models.ForeignKey(User,related_name="posts",on_delete=models.CASCADE)
    update_at = models.ForeignKey(User,null=True,related_name='+',on_delete=models.CASCADE)

    
