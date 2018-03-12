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
  def __init__(self):
    super(Management, self).__init__()
    self._path = os.path.dirname(__file__)
    if self._path not in sys.path:
      sys.path.append(self._path)
  
  def __str__(self):
    return '''
    Application management tool v.0.1.
    '''

  def runserver(self, address='127.0.0.1', port=5000):
    app.run(address, port)

  def initdb(self):
    try:
      DATABASE.connect()
      for table in MODEL_TABLES:
        if table.table_exists():
          DATABASE.drop_table(table)
        DATABASE.create_table(table)
    except OperationalError as e:
      print(e)

  def useradd(self, username, password):
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


if __name__ == '__main__':
  management = Fire(Management)
