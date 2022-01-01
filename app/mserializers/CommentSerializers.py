from rest_framework import serializers

from app.models.Comment import Comment
from app.mserializers.UserSerialziers import ProfileGeneralSerializer


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = '__all__'
    
    def get_author(self, comment):
        author_serializer = ProfileGeneralSerializer(comment.author)
        return author_serializer.data


class CommentCreateSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'time_stamp']
        
    def get_author(self, comment):
        author_serializer = ProfileGeneralSerializer(comment.author)
        return author_serializer.data