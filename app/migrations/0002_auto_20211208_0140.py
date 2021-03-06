# Generated by Django 3.2.9 on 2021-12-07 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LearnProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('streak_count', models.IntegerField(default=0)),
                ('total_exp', models.IntegerField(default=0)),
                ('last_learned', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'learn_progress',
            },
        ),
        migrations.AddField(
            model_name='myuser',
            name='learn_progress',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.learnprogress'),
        ),
    ]
