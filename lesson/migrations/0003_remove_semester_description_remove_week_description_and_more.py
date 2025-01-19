# Generated by Django 5.1.4 on 2025-01-18 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0002_semester_alter_lesson_day_alter_lesson_dayukr_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='semester',
            name='description',
        ),
        migrations.RemoveField(
            model_name='week',
            name='description',
        ),
        migrations.RemoveField(
            model_name='week',
            name='semester',
        ),
        migrations.AddField(
            model_name='semester',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='week',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='semester',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='week',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
