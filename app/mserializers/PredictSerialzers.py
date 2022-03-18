from rest_framework import serializers

class PredictLanguageSerializer(serializers.Serializer):
    paragraph = serializers.CharField(max_length=10000)