from rest_framework import viewsets
from .models import Course, Semester, Week, Lesson
from .serializers import CourseSerializer, SemesterSerializer, WeekSerializer, LessonSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, methods=['get'], url_path=r'(?P<semester_title>[-\w]+)/(?P<week_title>[-\w]+)/lessons')
    def lessons_for_week(self, request, pk=None, semester_title=None, week_title=None):
        try:
            course = self.get_object()
            semester = course.semesters.get(title__iexact=semester_title.replace('-', ' '))
            week = semester.weeks.get(title__iexact=week_title.replace('-', ' '))
            lessons = week.lessons.all()
            serializer = LessonSerializer(lessons, many=True)
            return Response(serializer.data)
        except (Course.DoesNotExist, Semester.DoesNotExist, Week.DoesNotExist):
            return Response({'error': 'Course, Semester, or Week not found'}, status=404)


class SemesterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer

class WeekViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Week.objects.all()
    serializer_class = WeekSerializer


class LessonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer