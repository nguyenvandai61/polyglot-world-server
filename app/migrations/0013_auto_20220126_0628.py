# Generated by Django 3.2.9 on 2022-01-25 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_question_explain'),
    ]

    operations = [
        migrations.AddField(
            model_name='learnprogress',
            name='daily_exp',
            field=models.JSONField(default='{}'),
        ),
        migrations.AddField(
            model_name='learnprogress',
            name='language',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.language'),
        ),
    ]
