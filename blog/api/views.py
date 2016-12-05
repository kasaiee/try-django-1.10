from rest_framework import generics

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import (
    SearchFilter, 
    OrderingFilter,
    )

from rest_framework.permissions import IsAdminUser, AllowAny

from blog.models import Blog, BlogGroup
from .permissions import OwnerCanManageOrReadOnly
from .pagination import (
    PostPageNumberPagination,
    PostLimitOffsetPagination
    )
from .serializers import (
    GroupListSerializer,
    GroupDetailSerializer,

    PostListSerializer,
    PostDetailSerializer,
    PostCreateSerializer,
    PostDeleteSerializer,
    )

from django.db.models import Q
from django.core.exceptions import PermissionDenied


########### POST SERIALIZER ###########
class PostListAPIView(generics.ListAPIView):
    '''
    write api documentation here in markdown syntax
    '''

    # we comment queryset because we defined get_queryset() function in this class
    # queryset = Blog.objects.all()
    
    serializer_class = PostListSerializer
    pagination_class = PostLimitOffsetPagination
    filter_backends = (
        DjangoFilterBackend, # work with filter_fields, Note that this backend imported from django_filters
        SearchFilter, # work with search_filds
        OrderingFilter # work with ordering_fields
        )
    filter_fields = (
        'title', 
        'content', 
        'createDateTime',
        'updateDateTime',
        'owner__username', 
        'owner__first_name', 
        'owner__last_name'
        )
    search_fields = (
        'title', 
        'content', 
        'owner',
        'owner__username', 
        'owner__first_name', 
        'owner__last_name'
        )
    ordering_fields = (
        'id', 
        'title', 
        'content', 
        'owner',
        'owner__username', 
        'owner__first_name', 
        'owner__last_name'
        )


    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_superuser:
            # superuser can see all posts
            queryset = Blog.objects.all()
        else:
            # otherwise every user can see his posts
            queryset = Blog.objects.filter(owner=self.request.user)

        # Custom search. It is not related to rest_framework
        query = self.request.GET.get('q')
        if query:
            # if user search for something by 'q' keyword
            queryset = queryset.filter(
                Q(title__icontains=query)|
                Q(content__icontains=query)|
                Q(owner__first_name__icontains=query)|
                Q(owner__last_name__icontains=query)|
                Q(owner__username__icontains=query)
                ).distinct().order_by('-updateDateTime')
        return queryset



class PostDetailAPIView(generics.RetrieveAPIView):
    '''
    write api documentation here in markdown syntax
    '''

    queryset = Blog.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'id'

class PostCreateAPIView(generics.CreateAPIView):
    '''
    write api documentation here in markdown syntax
    '''

    queryset = Blog.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = (IsAdminUser,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        # you can send email here and etc. this email send when serializer create


class PostDeleteAPIView(generics.RetrieveDestroyAPIView):
    '''
    write api documentation here in markdown syntax
    '''

    queryset = Blog.objects.all()
    serializer_class = PostDeleteSerializer
    permission_classes = (OwnerCanManageOrReadOnly,)
    lookup_field = 'id'

    def perform_destroy(self, serializer):
        # just owner can delete post
        if serializer.owner != self.request.user:
            raise PermissionDenied
        else:
            serializer.delete()
            # you can send email here and etc. this email send when serializer delete


class PostUpdateAPIView(generics.RetrieveUpdateAPIView):
    '''
    write api documentation here in markdown syntax
    '''

    queryset = Blog.objects.all()
    serializer_class = PostDeleteSerializer
    permission_classes = (OwnerCanManageOrReadOnly,)
    lookup_field = 'id'

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)
        # you can send email here and etc. this email send when serializer update


########### GROUP SERIALIZER ###########\
class GroupListAPIView(generics.ListAPIView):
    queryset = BlogGroup.objects.all()
    serializer_class = GroupListSerializer


class GroupDetailAPIView(generics.RetrieveAPIView):
    queryset = BlogGroup.objects.all()
    serializer_class = GroupDetailSerializer
    lookup_field = 'id'


########## USER SERIALIZER #########
from django.contrib.auth import get_user_model
User = get_user_model()
from serializers import (
    UserListSerializer,
    UserCreateSerializer,
    )

class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer