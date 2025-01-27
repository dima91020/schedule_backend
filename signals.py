# your_app_name/signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json
from lesson.models import Lesson

@receiver(post_save, sender=Lesson)
def lesson_saved_handler(sender, instance, created, **kwargs):
    action = 'created' if created else 'updated'
    message = {
        'action': action,
        'lesson': {
            'id': instance.id,
            'title': instance.title,
            'day': instance.dayUkr,
            'timeStart': instance.timeStart,
            'teacher': instance.teacher,
            'typeLesson': instance.typeLesson,
        },
    }
    send_to_websocket(message)

@receiver(post_delete, sender=Lesson)
def lesson_deleted_handler(sender, instance, **kwargs):
    message = {
        'action': 'deleted',
        'lesson': {
            'id': instance.id,
            'title': instance.title,
        },
    }
    send_to_websocket(message)

def send_to_websocket(message):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'lesson_updates',  # Назва групи для WebSocket
        {
            'type': 'lesson_update',  # Тип події
            'data': message,
        }
    )
