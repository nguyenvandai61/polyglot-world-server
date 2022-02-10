from datetime import datetime
from rest_framework import serializers
from app.models.LearnProgress import LearnProgress


class LearnProgressSerializer(serializers.ModelSerializer):
    today_exp = serializers.SerializerMethodField()
    class Meta:
        model = LearnProgress
        fields = '__all__'
    
    def get_today_exp(self, learn_progress):
        today = datetime.now().date().strftime('%Y-%m-%d')
        return learn_progress.lastest7dayexp[today]