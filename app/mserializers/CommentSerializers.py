from rest_framework import serializers

from app.models.Comment import Comment
from app.mserializers.UserSerialziers import ProfileGeneralSerializer


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    has_upvoted = serializers.SerializerMethodField()
    has_downvoted = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = '__all__'
    
    def get_author(self, comment):
        author_serializer = ProfileGeneralSerializer(comment.author)
        return author_serializer.data
    
    def get_has_upvoted(self, comment: Comment):
        return comment.has_upvoted(self.context['request'].user)
    
    def get_has_downvoted(self, comment: Comment):
        return comment.has_downvoted(self.context['request'].user)


class CommentCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ['content']


class CommentCreateResponseSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'time_stamp']
        
    def get_author(self, comment):
        author_serializer = ProfileGeneralSerializer(comment.author)
        return author_serializer.data
    
    
class CommentVoteSerializer(serializers.ModelSerializer):
    vote = serializers.ChoiceField(choices=[-1, 1])
    class Meta:
        model = Comment
        fields = ['vote']
        
class CommentVoteResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['n_upvote', 'n_downvote']