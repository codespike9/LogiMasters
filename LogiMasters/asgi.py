from channels.routing import URLRouter,ProtocolTypeRouter
import os
import fleet.routings
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LogiMasters.settings')

application=ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':URLRouter(fleet.routings.websocket_urlpatterns)
})