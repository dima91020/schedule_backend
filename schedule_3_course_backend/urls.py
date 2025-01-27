"""
URL configuration for schedule_3_course_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from lesson import views
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'courses', views.CourseViewSet)
router.register(r'semesters', views.SemesterViewSet)
router.register(r'weeks', views.WeekViewSet)
router.register(r'lessons', views.LessonViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/data-changed/', views.data_changed_check, name='data-changed-check'), # Ось що ми змінили
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
