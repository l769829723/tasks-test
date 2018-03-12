#! /usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import sys

from fire import Fire
from peewee import OperationalError
from main.app import app
from main.models import User
from main.models import DATABASE
from main.models import MODEL_TABLES


class Management(object):
  """
  简易的应用控制工具，提供快捷创建数据库，和创建用户的方式。
  """
  def __init__(self):
    '''
    初始化方法，检查当前路径是否在系统搜索路径中，如果不存在则添加。
    '''
    super(Management, self).__init__()
    self._path = os.path.dirname(__file__)
    if self._path not in sys.path:
      sys.path.append(self._path)
  
  def __str__(self):
    return '''
    应用程序管理控制台v0.1
    '''

  def runserver(self, address='127.0.0.1', port=5000):
    app.run(address, port)

  def initdb(self):
    '''
    根据定义的数据模型，创建数据表结构，该操作会清楚用户保存的已有数据。
    '''
    try:
      DATABASE.connect()
      for table in MODEL_TABLES:
        if table.table_exists():
          DATABASE.drop_table(table)
        DATABASE.create_table(table)
    except OperationalError as e:
      print(e)

  def useradd(self, username, password):
    '''
    添加一个用户，如果用户存在则更新用户名和密码。
    :username 要添加或更新的用户名称
    :password 用户要设置或者更新的密码
    '''
    user = User.select().where(User.username == username).first()
    if user:
      user.password = password
    else:
      user = User()
      user.username = username
      user.password = password
      user.role = 'ADMIN'
      user.locked = False
    user.save()

  def help(self, option):
    try:
      doc = getattr(self, option).__doc__
      print('Usage:\t\t{}\n{}'.format(option, doc.lstrip()))
    except AttributeError:
      print('Invalid option.')


if __name__ == '__main__':
  management = Fire(Management)
