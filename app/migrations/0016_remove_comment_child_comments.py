# Generated by Django 3.2.9 on 2022-02-21 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_learnprogress_lastest7dayexp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='child_comments',
        ),
    ]