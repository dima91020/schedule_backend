# Generated by Django 5.1.4 on 2025-01-19 02:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0004_delete_semester_remove_lesson_week_delete_week'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='count',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='day',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='dayUkr',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='isElective',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='timeStart',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='typeLesson',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='usersId',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='zoomURL',
        ),
        migrations.AddField(
            model_name='lesson',
            name='content',
            field=models.TextField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('order', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='semesters', to='lesson.course')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('order', models.IntegerField()),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weeks', to='lesson.semester')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.AddField(
            model_name='lesson',
            name='week',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='lesson.week'),
        ),
    ]
