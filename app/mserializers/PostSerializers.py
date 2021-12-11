from rest_framework import serializers

from app.models.Post import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post