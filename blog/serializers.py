from rest_framework import serializers
from .models import Post, Comment


class PostSerilizer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')


    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('author',)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('author', 'post')

