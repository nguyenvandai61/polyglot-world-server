# Generated by Django 3.2.9 on 2022-01-16 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('MCQ', 'Multiple Choice Question'), ('TF', 'True or False Question'), ('SA', 'Short Answer Question')], default='MCQ', max_length=3),
        ),
    ]