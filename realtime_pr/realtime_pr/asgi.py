import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from django.urls import path
from channels.generic.websocket import WebsocketConsumer
import json
from time import sleep
from random import randint

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'realtime_pr.settings')

class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        for i in range(1000):
            self.send(json.dumps({'message': randint(1, 100)}))
            sleep(1)

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        pass

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path('ws/some_url/', WSConsumer.as_asgi()),
        ])
    ),
})
