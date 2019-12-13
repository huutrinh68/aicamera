from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url, include
from django.urls import path, re_path

from streamer.consumers import StreamerConsumer


application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
                path('streamer', StreamerConsumer),
            ])
        )
    ),
})