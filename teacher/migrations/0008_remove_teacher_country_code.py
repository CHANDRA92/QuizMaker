# Generated by Django 4.2.7 on 2023-11-26 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0007_teacher_country_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='country_code',
        ),
    ]
