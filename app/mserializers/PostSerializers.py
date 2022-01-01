from django.db.models import fields
from rest_framework import serializers

from app.models.Post import Post
from app.mserializers.UserSerialziers import ProfileGeneralSerializer
from app.mserializers.CommentSerializers import CommentSerializer


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    is_hearted = serializers.SerializerMethodField()
    first_comment = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = '__all__'
    
    def get_author(self, post):
        author_serializer = ProfileGeneralSerializer(post.author)
        return author_serializer.data
    
    def get_is_hearted(self, post):
        author = post.author
        return author.is_hearted(post.id)
    
    def get_first_comment(self, post):
        if post.comments.count() == 0:
            return None
        else:
            comment_serializer = CommentSerializer(post.comments.first())
            return comment_serializer.data
        
        
class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'