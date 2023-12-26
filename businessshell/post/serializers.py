from rest_framework import serializers
from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'author',
            'body',
            'created',
        )


class PostSerializers(serializers.ModelSerializer):
    comment = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = (
            'title',
            'author',
            'body',
            'comment',
            'created',
        )


class PostsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title',
            'author',
            'body',
            'created',
        )
