import os
import sys

from fire import Fire
from main import app


class Management(Fire):
  def __init__(self):
    super(Management, self).__init__()
    self._path = os.path.dirname(__file__)
    if self._path not in sys.path:
      sys.path.append(self._path)
  
  def runserver(self, address='127.0.0.1', port=5000):
    app.run(address, port)


if __name__ == '__main__':
  management = Management()
