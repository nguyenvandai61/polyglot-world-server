# Generated by Django 3.2.9 on 2021-12-22 19:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20211221_0145'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hearts',
            field=models.ManyToManyField(blank=True, related_name='hearts', to=settings.AUTH_USER_MODEL),
        ),
    ]