from rest_framework import serializers
from .models import Lesson

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'count', 'title', 'day', 'dayUkr', 'timeStart', 'zoomURL', 'teacher', 'typeLesson', 'isElective', 'usersId')