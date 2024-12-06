import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        # 
        self.accept()

    def disconnect(self, close_code):
        pass

    
    # receive message from WebSocket
    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # send message to WebSocket
        self.send(text_data = json.dumps({'message': message}))
