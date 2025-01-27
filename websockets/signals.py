from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from lesson.models import Lesson   # Замініть на свою модель

@receiver(post_save, sender=Lesson)
@receiver(post_delete, sender=Lesson)
def notify_model_change(sender, instance, **kwargs):
    # Отримуємо канал для зв'язку
    channel_layer = get_channel_layer()
    message = {
        "type": "send_update",
        "message": {"id": instance.id, "status": "changed"},
    }
    # Відправляємо повідомлення всім у групі
    async_to_sync(channel_layer.group_send)("model_changes", message)
