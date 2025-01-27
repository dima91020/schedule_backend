from django.urls import path
from .consumers import ModelChangeConsumer

websocket_urlpatterns = [
    path('ws/updates/', ModelChangeConsumer.as_asgi()),
]
