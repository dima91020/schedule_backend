import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ModelChangeConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Додаємо користувача до групи для отримання оновлень
        await self.channel_layer.group_add("model_changes", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Видаляємо користувача з групи
        await self.channel_layer.group_discard("model_changes", self.channel_name)

    async def send_update(self, event):
        # Відправляємо повідомлення клієнту
        await self.send(text_data=json.dumps(event["message"]))
