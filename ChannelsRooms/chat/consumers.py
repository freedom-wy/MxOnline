# chat/consumers.py
from channels.generic.websocket import WebsocketConsumer
import json


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        # 接收从客户端发来的消息
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # 拿到客户端消息后向客户端发回
        self.send(text_data=json.dumps({
            'message': message
        }))
