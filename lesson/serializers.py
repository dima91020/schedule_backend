from rest_framework import serializers
from .models import Course, Semester, Week, Lesson

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class WeekSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)
    class Meta:
        model = Week
        fields = ['id', 'title', 'order', 'lessons']

class SemesterSerializer(serializers.ModelSerializer):
    weeks = WeekSerializer(many=True, read_only=True)
    class Meta:
      model = Semester
      fields = ['id', 'title', 'order', 'weeks']


class CourseSerializer(serializers.ModelSerializer):
    semesters = SemesterSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = ['id', 'title', 'semesters']
