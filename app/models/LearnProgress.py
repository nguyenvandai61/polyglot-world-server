from django.db import models

class LearnProgress(models.Model):
    streak_count = models.IntegerField(default=0, null=False, blank=False)
    total_exp = models.IntegerField(default=0, null=False, blank=False)
    last_learned = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    level = property(lambda self: self.get_level())

    class Meta:
        db_table = 'learn_progress'

    def __str__(self):
        return f'{self.streak_count} days/{self.total_exp} exp'

    def get_level(self):
        return self.total_exp // 1000 + 1
        
