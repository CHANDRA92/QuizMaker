# Generated by Django 4.2.7 on 2023-11-16 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0016_result_testno_alter_question_marks_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='exam',
        ),
    ]
