from django.shortcuts import render
from rest_framework import generics
from .models import Post, PostCategory, Author
from .serializers import PostCategorySerializer, PostSerializer, AuthorSerializer

# Create your views here.


class PostCategoryList(generics.ListCreateAPIView):
    queryset = PostCategory.objects.all()
    serializer_class = PostCategorySerializer
    name = 'postcategory-list'
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['name']


class PostCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostCategory.objects.all()
    serializer_class = PostCategorySerializer
    name = 'postcategory-detail'


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-detail'


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-list'
    filterset_fields = ['title']
    ordering_fields = ['title']
