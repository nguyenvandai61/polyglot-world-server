from django import db
from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name
    
    def create(self, name, code, description):
        self.name = name
        self.code = code
        self.description = description
        self.save()
        return self

    class Meta:
        db_table = 'language'
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'
        ordering = ['name']
        
