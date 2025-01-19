# Generated by Django 5.1.4 on 2025-01-19 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0005_course_remove_lesson_count_remove_lesson_day_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='count',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='lesson',
            name='day',
            field=models.CharField(choices=[('Mon', 'Monday'), ('Tues', 'Tuesday'), ('Wed', 'Wednesday'), ('Thurs', 'Thursday'), ('Fri', 'Friday'), ('Sat', 'Saturday')], default=('пн', 'Понеділок'), max_length=10),
        ),
        migrations.AddField(
            model_name='lesson',
            name='dayUkr',
            field=models.CharField(choices=[('пн', 'Понеділок'), ('вт', 'Вівторок'), ('ср', 'Середа'), ('чт', 'Четвер'), ('пт', "П'ятниця"), ('сб', 'Субота')], default=('пн', 'Понеділок'), max_length=2),
        ),
        migrations.AddField(
            model_name='lesson',
            name='isElective',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='lesson',
            name='teacher',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='lesson',
            name='timeStart',
            field=models.CharField(choices=[('8-30', '8-30'), ('10-25', '10-25'), ('12-20', '12-20'), ('14-15', '14-15'), ('16-10', '16-10'), ('18-30', '18-30')], default='8-30', max_length=10),
        ),
        migrations.AddField(
            model_name='lesson',
            name='typeLesson',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='lesson',
            name='usersId',
            field=models.JSONField(default=None),
        ),
        migrations.AddField(
            model_name='lesson',
            name='zoomURL',
            field=models.URLField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
