from django.db import models

# Create your models here.

class Lesson(models.Model):
    DAYS_OF_WEEK = [
        ('Mon', 'Monday'),
        ('Tues', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thurs', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
    ]

    DAYS_OF_WEEK_UKR = [
        ('пн', 'Понеділок'),
        ('вт', 'Вівторок'),
        ('ср', 'Середа'),
        ('чт', 'Четвер'),
        ('пт', "П'ятниця"),
        ('сб', 'Субота'),
    ]

    TIME_FOR_LESSON = [
        ('8-30', '8-30'),
        ('10-25', '10-25'),
        ('12-20', '12-20'),
        ('14-15', '14-15'),
        ('16-10', '16-10'),
        ('18-30', '18-30'),
    ]

    count = models.PositiveIntegerField()
    title = models.CharField(max_length=200)
    day = models.CharField(
        max_length=10,
        choices=DAYS_OF_WEEK,
    )
    dayUkr = models.CharField(
        max_length=2,
        choices=DAYS_OF_WEEK_UKR,
    )
    timeStart = models.CharField(
        max_length=10,
        choices=TIME_FOR_LESSON,
    )
    zoomURL = models.URLField(blank=True, null=True)
    teacher = models.CharField(max_length=100)
    typeLesson = models.CharField(max_length=100)
    isElective = models.BooleanField(default=False)
    usersId = models.JSONField()

    def __str__(self):
        return f"{self.title}, ({self.dayUkr}), ({self.timeStart})"
