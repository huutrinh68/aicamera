import asyncio 
import json
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from asgiref.sync import async_to_sync
import base64
import numpy as np
import cv2

image_file='decode.png'

class StreamerConsumer(AsyncJsonWebsocketConsumer):

    # Join group
    async def connect(self):
        self.group_name = "streamer"
        
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()
        print('###Client Connected')
        print(f'Add {self.channel_name} channel to group {self.group_name}')

    # Leave group
    async def disconnect(self, code):
        
        await self.channel_layer.group_discard(
            self.group_name, 
            self.channel_name
        )
        print('###Client Disconnect')
        print(f'Remove {self.channel_name} channel from group {self.group_name}')

    # Receive message from websocket client
    async def receive(self, text_data=None, bytes_data=None):
        text_data = text_data.split('base64,')[1]
        img_binary = base64.urlsafe_b64decode(text_data)
        png = np.frombuffer(img_binary, dtype=np.uint8)
        img = cv2.imdecode(png, cv2.IMREAD_COLOR)
        cv2.imwrite(image_file, img)
        print('SAVED!!!!!')

        # print(f'receive: {text_data}')

        # Send message group
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'update_frame',
                'data': text_data
            }
        )

    async def update_frame(self, event):
        # message = event['message']

        # Send message to WebSocket
        # await self.send(event)
        # print(f'frame update {event}')
        pass

