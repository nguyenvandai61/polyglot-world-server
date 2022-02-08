import imp

from rest_framework import serializers
from app.models.Question import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'content', 'type', 'exp', 'n_upvote', 'n_downvote', 'answers', 'right_answer', 'explain')


class QuestionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'author', 'content', 'type', 'exp', 'answers', 'right_answer', 'explain')
        
        
class QuestionVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'upvote', 'downvote')
    
    
class QuestionSubmitAnswerSerializer(serializers.Serializer):
    answer = serializers.CharField()
    
class QuestionWithoutRAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'content', 'type', 'exp', 'answers')