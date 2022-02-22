from rest_framework import serializers

from app.models.Comment import Comment
from app.mserializers.UserSerialziers import ProfileGeneralSerializer


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    has_upvoted = serializers.SerializerMethodField()
    has_downvoted = serializers.SerializerMethodField()
    child_comments = serializers.SerializerMethodField()
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
    
    def get_child_comments(self, comment: Comment, *args, **kwargs):
        kwargs.setdefault('context', {})['request'] = self.context['request']
        comment_serializer = ChildCommentsSerializer(comment, **kwargs)
        return comment_serializer.data.get('child_comments')


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

       
class ChildCommentsSerializer(serializers.ModelSerializer):
    child_comments = serializers.SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = ['child_comments']
        
    def get_child_comments(self, comment, *args, **kwargs):        
        child_comments = Comment.objects.filter(parent_comment=comment).order_by('time_stamp')
        kwargs.setdefault('context', {})['request'] = self.context['request']
        child_comments_serializer = CommentSerializer(child_comments, many=True, **kwargs)
        return child_comments_serializer.data