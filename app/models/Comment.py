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
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.content

    class Meta:
        db_table = 'comment'
        ordering = ['-time_stamp']
    
    def create(self, author, post, content, parent=None):
        self.author = author
        self.post = post
        self.content = content
        self.parent_comment = parent
        self.save()
        return self
    
    def has_upvoted(self, user):
        return self.upvotes.filter(id=user.id).exists()
    
    def has_downvoted(self, user):
        return self.downvotes.filter(id=user.id).exists()
    