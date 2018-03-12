from sanic.response import json
from sanic.views import HTTPMethodView
from main.models import User


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


class APIUsers(HTTPMethodView):
  def get(self, request):
    users = [user.to_dict() for user in User.select()]
    return json({'users': users})
