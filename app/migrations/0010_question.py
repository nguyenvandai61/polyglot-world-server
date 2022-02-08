# Generated by Django 3.2.9 on 2022-01-15 08:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_comment_parent_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default='')),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(default='question', max_length=20)),
                ('exp', models.IntegerField(default=0)),
                ('n_upvote', models.IntegerField(default=0)),
                ('n_downvote', models.IntegerField(default=0)),
                ('answers', models.JSONField(default='')),
                ('right_answer', models.TextField(default='')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('downvote', models.ManyToManyField(blank=True, related_name='downvote', to=settings.AUTH_USER_MODEL)),
                ('upvote', models.ManyToManyField(blank=True, related_name='upvote', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'question',
                'ordering': ['-time_stamp'],
            },
        ),
    ]
