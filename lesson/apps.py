# lesson/apps.py
from django.apps import AppConfig
from django.utils import timezone


class LessonConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lesson'

    def ready(self):
        import lesson.signals
        from lesson.signals import update_last_modified_timestamp
        update_last_modified_timestamp(None, None)  # Ініціалізуємо _last_change_timestamp