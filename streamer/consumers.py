import asyncio 
import json
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from asgiref.sync import async_to_sync

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
        print(f'receive: {text_data}')

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
        print(f'frame update {event}')

