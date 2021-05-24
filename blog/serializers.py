from rest_framework import serializers
from .models import Author, Post, PostCategory
from django.contrib.auth.models import User


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='author-detail')

    class Meta:
        model = Author
        fields = ['pk', 'url', 'name', 'nickname', 'firstname', 'lastname', 'birthday', 'about', 'author']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    post_category = serializers.SlugRelatedField(queryset=PostCategory.objects.all(), slug_field='name')
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())

    class Meta:
        model = Post
        fields = ['pk', 'url', 'title', 'content', 'publication_date', 'post_category', 'author']


class PostCategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PostCategory
        fields = ['pk', 'url', 'name', 'posts']
