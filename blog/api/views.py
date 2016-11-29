from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .serializers import (
    PostListSerializer,
    PostDetailSerializer,
    PostCreateSerializer,
    )
from blog.models import Blog


class PostListAPIView(generics.ListAPIView):
    '''
    **this is a **
    simple documentation for api
    '''

    queryset = Blog.objects.all()
    serializer_class = PostListSerializer


class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'id'

class PostCreateAPIView(generics.CreateAPIView):
    '''
    **this is a **
    simple documentation for api
    '''

    queryset = Blog.objects.all()
    serializer_class = PostCreateSerializer
    permissions_classes = ('IsAdminUser',)
