# Generated by Django 5.1.4 on 2025-01-18 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0003_remove_semester_description_remove_week_description_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Semester',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='week',
        ),
        migrations.DeleteModel(
            name='Week',
        ),
    ]