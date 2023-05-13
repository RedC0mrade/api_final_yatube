from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from django.contrib.auth import get_user_model

from posts.models import Comment, Group, Follow, Post

User = get_user_model()


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'slug', 'description')
        model = Group


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = ('id', 'text', 'author', 'group', 'pub_date')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = ('id', 'text', 'post', 'created', 'author')
        model = Comment
        read_only_fields = ('post',)


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True, slug_field='username')
    following = serializers.SlugRelatedField(
        read_only=False, slug_field='username', queryset=User.objects.all())

    def validate_following(self, value):
        if value == self.context['request'].user:
            raise serializers.ValidationError('Нельзя подписаться на себя')
        return value

    class Meta:
        fields = ('id', 'following', 'user')
        model = Follow
