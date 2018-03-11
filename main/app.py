from sanic import Sanic
from main import settings
from apis.views import APIRoot

app = Sanic(__name__)

app.config.from_object(settings)

app.add_route(APIRoot.as_view(), '/api/v1/')
