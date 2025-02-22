# Generated by Django 5.1.4 on 2025-01-14 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=200)),
                ('day', models.CharField(max_length=10)),
                ('dayUkr', models.CharField(max_length=10)),
                ('timeStart', models.CharField(max_length=10)),
                ('zoomURL', models.URLField(blank=True, null=True)),
                ('teacher', models.CharField(max_length=100)),
                ('typeLesson', models.CharField(max_length=100)),
                ('isElective', models.BooleanField(default=False)),
                ('usersId', models.JSONField()),
            ],
        ),
    ]
