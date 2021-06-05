from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .models import Post, PostCategory, Author
from .serializers import PostCategorySerializer, PostSerializer, AuthorSerializer, UserSerializer
from django.contrib.auth.models import User
from .custompermission import IsCurrentUserOwnerOrReadOnly

# Create your views here.


class PostCategoryList(generics.ListCreateAPIView):
    queryset = PostCategory.objects.all()
    serializer_class = PostCategorySerializer
    name = 'postcategory-list'
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['name']
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


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
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsCurrentUserOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    name = 'author-list'


class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    name = 'author-detail'


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'post-categories': reverse(PostCategoryList.name, request=request),
            'posts': reverse(PostList.name, request=request),
            'users': reverse(UserList.name, request=request),
            'authors': reverse(AuthorList.name, request=request),
        })
