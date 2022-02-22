from datetime import datetime, timedelta
from rest_framework import serializers
from app.models.LearnProgress import LearnProgress


class LearnProgressSerializer(serializers.ModelSerializer):
    today_exp = serializers.SerializerMethodField()
    lastest7dayexp = serializers.SerializerMethodField()
    class Meta:
        model = LearnProgress
        fields = '__all__'
    
    def get_lastest7dayexp(self, learn_progress: LearnProgress):
        if (learn_progress.lastest7dayexp is None):
            return {}
        return learn_progress.lastest7dayexp
    
    def get_today_exp(self, learn_progress):
        today = datetime.now().date().strftime('%Y-%m-%d')
        if (learn_progress.lastest7dayexp is None):
            return 0
        if learn_progress.lastest7dayexp.get(today) is None:
            return 0
        return learn_progress.lastest7dayexp[today]