# Generated by Django 4.2.7 on 2023-11-16 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0015_alter_question_marks_alter_question_testno'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='testno',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quiz.testdetails'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='marks',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='testdetails',
            name='question_number',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='testdetails',
            name='total_marks',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
