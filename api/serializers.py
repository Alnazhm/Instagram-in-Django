from rest_framework import serializers
from posts.models import Post, Comment, Like
from accounts.models import Account


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'username', 'email', 'avatar', 'first_name',
                  'additional', 'phone', 'gender', 'liked_posts', 'subscriptions', 'commented_posts',
                  'created_at', 'updated_at', )
        read_only_fields = ('id','password', 'created_at', 'updated_at', 'is_deleted')


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'is_like', 'author', 'posts', 'updated_at', 'created_at')
        read_only_fields = ('id', 'created_at', 'updated_at')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'description', 'author', 'image', 'comments_count',
                   'likes_count', 'is_deleted', 'updated_at', 'created_at')
        read_only_fields = ('id', 'created_at', 'updated_at',  'is_deleted')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'updated_at', 'created_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

