from channels.generic.websocket import WebsocketConsumer
import json
from random import randint
from time import sleep

class WSConsumer(WebsocketConsumer):
    def connect(self):
        print("WebSocket connected")
        self.accept()
        
        for i in range(1000):
            self.send(json.dumps({'message': randint(1, 100)}))
            sleep(1)

    def disconnect(self, close_code):
        print("WebSocket disconnected", close_code)

    def receive(self, text_data):
        print("Received message", text_data)
