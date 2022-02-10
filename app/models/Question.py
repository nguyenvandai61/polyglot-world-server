from turtle import down
from django.db import models

QUESTION_TYPE_CHOICES = (
    ('MCQ', 'Multiple Choice Question'),
    ('TF', 'True or False Question'),
    ('SA', 'Short Answer Question')
)


class Question(models.Model):
    author = models.ForeignKey('MyUser', on_delete=models.CASCADE)
    content = models.TextField(default='')
    time_stamp = models.DateTimeField(auto_now_add=True)
    upvote = models.ManyToManyField(
        'MyUser', related_name='upvote', blank=True)
    downvote = models.ManyToManyField(
        'MyUser', related_name='downvote', blank=True)
    type = models.CharField(choices=QUESTION_TYPE_CHOICES, default='MCQ', null=False, max_length=3)
    exp = models.IntegerField(default=0)
    n_upvote = models.IntegerField(default=0)
    n_downvote = models.IntegerField(default=0)
    answers = models.JSONField(default='')
    right_answer = models.TextField(default='')
    explain = models.TextField(default='')

    def __str__(self):
        return self.content

    class Meta:
        db_table = 'question'
        ordering = ['-time_stamp']
