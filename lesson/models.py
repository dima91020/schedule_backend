from django.db import models

# Create your models here.

class Lesson(models.Model):
    count = models.PositiveIntegerField()
    title = models.CharField(max_length=200)
    day = models.CharField(max_length=10)
    dayUkr = models.CharField(max_length=10)
    timeStart = models.CharField(max_length=10)
    zoomURL = models.URLField(blank=True, null=True)
    teacher = models.CharField(max_length=100)
    typeLesson = models.CharField(max_length=100)
    isElective = models.BooleanField(default=False)
    usersId = models.JSONField()

    def __str__(self):
        return f"{self.title}, ({self.dayUkr}), ({self.timeStart})"
