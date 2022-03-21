from datetime import datetime
import imp

from rest_framework import serializers
from app.models.Question import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'content', 'type', 'exp', 'n_upvote', 'n_downvote', 'answers', 'right_answer', 'explain', 'time_limit', 'time_stamp')


class QuestionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'author', 'content', 'type', 'exp', 'answers', 'right_answer', 'explain', 'time_limit')
        
        
class QuestionVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'upvote', 'downvote')
    
    
class QuestionSubmitAnswerSerializer(serializers.Serializer):
    answer = serializers.CharField()
    token = serializers.CharField()
    
class QuestionWithoutRAnswerSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    class Meta:
        model = Question
        fields = ('id', 'content', 'type', 'exp', 'answers', 'time_limit', 'token')
        
    def get_token(self, question: Question):
        user = self.context['request'].user
        time_now = datetime.now()
        return str.format('{}ptoken{}', user.id, time_now.strftime('%Y%m%d%H%M%S'))