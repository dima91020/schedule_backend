# lesson/signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils import timezone
from .models import Course, Semester, Week, Lesson

_last_change_timestamp = None  # Приватна змінна

def get_last_change_timestamp():
    global _last_change_timestamp
    return _last_change_timestamp

def update_last_modified_timestamp(sender, instance, **kwargs):
    global _last_change_timestamp
    _last_change_timestamp = timezone.now()


post_save.connect(update_last_modified_timestamp, sender=Course)
post_save.connect(update_last_modified_timestamp, sender=Semester)
post_save.connect(update_last_modified_timestamp, sender=Week)
post_save.connect(update_last_modified_timestamp, sender=Lesson)

post_delete.connect(update_last_modified_timestamp, sender=Course)
post_delete.connect(update_last_modified_timestamp, sender=Semester)
post_delete.connect(update_last_modified_timestamp, sender=Week)
post_delete.connect(update_last_modified_timestamp, sender=Lesson)