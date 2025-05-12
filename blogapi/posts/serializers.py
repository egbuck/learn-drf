from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Post

class PostSerializer(serializers.ModelSerializer):
    # Use SlugRelatedField to display username, but for serialization
    # (inputs for creating/updating) it will still use the user ID
    author = serializers.SlugRelatedField(
        queryset=get_user_model().objects.all(), slug_field="username"
    )
    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'body', 'created_at',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email',)