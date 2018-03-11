from sanic.response import json
from sanic.views import HTTPMethodView


class APIRoot(HTTPMethodView):
  
  def get(self, request):
    data = {
      'msg': 'Hello Sanic API.',
      'version': 'v1',
      'urls': [
        'apples',
        'juices'
      ]
    }
    return json(data)
