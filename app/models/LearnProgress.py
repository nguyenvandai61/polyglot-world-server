from django.db import models

class LearnProgress(models.Model):
    streak_count = models.IntegerField(default=0, null=False, blank=False)
    total_exp = models.IntegerField(default=0, null=False, blank=False)
    # lastest7dayexp = {
    #     '2020-01-15': 1000,
    #     '2020-01-16': 2000,
    # }
    lastest7dayexp = models.JSONField(default=None, null=True, blank=True)
    language = models.ForeignKey('Language', on_delete=models.CASCADE, default=1)
    level = property(lambda self: self.get_level())

    class Meta:
        db_table = 'learn_progress'

    def __str__(self):
        return f'{self.streak_count} days/{self.total_exp} exp'

    def get_level(self):
        return self.total_exp // 1000 + 1
        
