from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import (
    CurrentUserDefault,
    ModelSerializer,
    PrimaryKeyRelatedField,
    SlugRelatedField,
    UniqueTogetherValidator,
    ValidationError,
)

from posts.models import Comment, Follow, Group, Post

User = get_user_model()


class PostSerializer(ModelSerializer):

    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(ModelSerializer):

    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    post = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment


class FollowSerializer(ModelSerializer):

    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=CurrentUserDefault(),
    )
    following = SlugRelatedField(
        queryset=User.objects.all(), slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
                message='Вы уже подписаны на этого автора!',
            )
        ]

    def validate(self, data):
        """Проверка на подписку на самого себя."""
        if self.context['request'].user == data['following']:
            raise ValidationError('Нельзя подписаться на самого себя!')
        return data


class GroupSerializer(ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Group
