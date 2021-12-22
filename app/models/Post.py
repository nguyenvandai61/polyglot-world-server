from django import db
from django.db import models
from .Comment import Comment
class Post(models.Model):
    author = models.ForeignKey('MyUser', on_delete=models.CASCADE)
    content = models.TextField(default='')
    time_stamp = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    language = models.ForeignKey('Language', on_delete=models.CASCADE)
    hearts = models.ManyToManyField('MyUser', related_name='hearts', blank=True)
    comments = models.ManyToManyField(Comment, related_name='comments', blank=True)
    n_heart = models.IntegerField(default=0)
    n_comment = models.IntegerField(default=0)
    n_share = models.IntegerField(default=0)
    
    def __str__(self):
        return self.content
    
    class Meta:
        db_table = 'post'
        ordering = ['-time_stamp']