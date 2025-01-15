from django.contrib import admin
from .models import Lesson

class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'count', 'title', 'day', 'dayUkr', 'timeStart', 'zoomURL', 'teacher', 'typeLesson', 'isElective', 'usersId')

# Register your models here.

admin.site.register(Lesson, LessonAdmin)
