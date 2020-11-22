'''
Author: huangjy
Date: 2020-11-22 08:59:39
LastEditors: huangjy
LastEditTime: 2020-11-22 10:02:18
Description: models api 学习和使用
'''
from boards.models import Board 


#创建对象
board = Board(name='java',description='java is good language')
#保存对象
board.save()
#访问字段的值
board.id
board.name
board.description
#更新字段
board.description = "This is effective java"
board.description
#每个Django模型都带有一个特殊的属性; 我们称之为模型管理器(Model Manager) 可通过objects 访问
#通过objects 创建新对象
board = Board.objects.create(name="Python",description="General discussion about Python")

#>>> Board.objects.all()
# <QuerySet [<Board: Board object (1)>, <Board: Board object (2)>, <Board: Board object (3)>]>
#未实现 Board 的__str__ 方法。__str__方法是对象的字符串表示形式
# 定义之后展示
#<QuerySet [<Board: 板块id：1, 板块名称：Django>, <Board: 板块id：2, 板块名称：java>, <Board: 板块id：3, 板块名称：Python>]>

#获取指定id的内容
Board.objects.get(id=3)
Board.objects.get(name='django')