from django.db import models

class Course(models.Model):
     title = models.CharField(max_length=255)
     updated_at = models.DateTimeField(auto_now=True)  # Додано поле

     def __str__(self):
         return self.title

class Semester(models.Model):
     course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='semesters')
     title = models.CharField(max_length=255)
     order = models.IntegerField()
     updated_at = models.DateTimeField(auto_now=True)  # Додано поле

     def __str__(self):
         return f"{self.course.title} - {self.title}"

     class Meta:
         ordering = ['order']

class Week(models.Model):
     semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='weeks')
     title = models.CharField(max_length=255)
     order = models.IntegerField()
     updated_at = models.DateTimeField(auto_now=True)  # Додано поле

     def __str__(self):
         return f"{self.semester.title} - {self.title}"

     class Meta:
         ordering = ['order']

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

     count = models.PositiveIntegerField(blank=True, default=0)
     title = models.CharField(max_length=200)
     day = models.CharField(
         max_length=10,
         choices=DAYS_OF_WEEK,
         default=DAYS_OF_WEEK[0][0],
     )
     dayUkr = models.CharField(
         max_length=2,
         choices=DAYS_OF_WEEK_UKR,
         default=DAYS_OF_WEEK_UKR[0][0],
     )
     timeStart = models.CharField(
         max_length=10,
         choices=TIME_FOR_LESSON,
         default=TIME_FOR_LESSON[0][0],
     )
     zoomURL = models.URLField(blank=True, null=True, default=None)
     teacher = models.CharField(max_length=100, default=None)
     typeLesson = models.CharField(max_length=100, default=None)
     isElective = models.BooleanField(default=False)
     usersId = models.JSONField(default=None, null=True, blank=True)
     updated_at = models.DateTimeField(auto_now=True)  # Додано поле

     week = models.ForeignKey(Week, on_delete=models.CASCADE, related_name='lessons', null=True, blank=True)

     def __str__(self):
         return f"{self.title}, ({self.dayUkr}), ({self.timeStart})"

     def save(self, *args, **kwargs):
         if not self.isElective and self.usersId is None:  # Змінена умова
             self.usersId = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

         super().save(*args, **kwargs)