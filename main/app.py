from sanic import Sanic
from main import settings
from apis.views import APIRoot
from apis.views import APIUsers

app = Sanic(__name__)

app.config.from_object(settings)

app.add_route(APIRoot.as_view(), '/api/v1/')
app.add_route(APIUsers.as_view(), '/api/v1/users')
