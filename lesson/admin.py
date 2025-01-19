from django.contrib import admin
from .models import Course, Semester, Week, Lesson

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

admin.site.register(Semester)
admin.site.register(Week)
admin.site.register(Lesson)