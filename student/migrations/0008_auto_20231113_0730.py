# Generated by Django 3.0.5 on 2023-11-13 07:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_remove_student_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.EmailField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='mobile',
            field=models.CharField(max_length=12, validators=[django.core.validators.MinLengthValidator(limit_value=10)]),
        ),
    ]
