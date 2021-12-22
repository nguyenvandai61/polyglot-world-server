from django import db
from django.db import models


class Comment(models.Model):
    author = models.ForeignKey('MyUser', on_delete=models.CASCADE)
    content = models.TextField(default='')
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    upvotes = models.ManyToManyField('MyUser', related_name='upvotes', blank=True)
    downvotes = models.ManyToManyField('MyUser', related_name='downvotes', blank=True)
    n_upvote = models.IntegerField(default=0)
    n_downvote = models.IntegerField(default=0)
    child_comments = models.ManyToManyField('self', related_name='child_comments', blank=True)

    def __str__(self):
        return self.content

    class Meta:
        db_table = 'comment'
        ordering = ['-time_stamp']
        
    def create(self, author, post, content):
        self.author = author
        self.post = post
        self.content = content
        self.save()
        return self