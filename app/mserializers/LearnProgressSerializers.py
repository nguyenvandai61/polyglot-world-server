from rest_framework import serializers
from app.models.LearnProgress import LearnProgress


class LearnProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearnProgress
        fields = '__all__'