from rest_framework import serializers
from .models import Author, Post, PostCategory
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'pk', 'username']


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Author
        fields = ['pk', 'url', 'about', 'user']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    post_category = serializers.SlugRelatedField(queryset=PostCategory.objects.all(), slug_field='name')
    author = AuthorSerializer()

    class Meta:
        model = Post
        fields = ['pk', 'url', 'title', 'content', 'publication_date', 'post_category', 'author']


class PostCategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PostCategory
        fields = ['pk', 'url', 'name', 'posts']
