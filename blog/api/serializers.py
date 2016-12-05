from blog.models import Blog, BlogGroup
from rest_framework.serializers import (
    ModelSerializer, 
    HyperlinkedIdentityField,
    SerializerMethodField,

    #relations
    StringRelatedField,
    PrimaryKeyRelatedField,
    HyperlinkedRelatedField,
    SlugRelatedField,
    )


post_detail_url = HyperlinkedIdentityField(
    view_name='blog-api:post-detail',
    lookup_field='id'
    )


post_delete_url = HyperlinkedIdentityField(
    view_name='blog-api:post-delete',
    lookup_field='id'
    )


post_update_url = HyperlinkedIdentityField(
    view_name='blog-api:post-update',
    lookup_field='id'
    )


class PostListSerializer(ModelSerializer):
    # HyperlinkedIdentityField
    detail_url = post_detail_url
    delete_url = post_delete_url
    update_url = post_update_url
    
    # SerializerMethodFields
    owner = SerializerMethodField()
    group = SerializerMethodField()

    class Meta:
        model = Blog
        # fields = ('id', 'title', 'owner', 'group', 'detail_url', 'update_url', 'delete_url')
        fields = ('id', 'title', 'owner', 'group', 'detail_url', 'delete_url', 'update_url')
        # extra_kwargs = {'title': {'write_only': False}}

    # get SerializerMethodField
    def get_owner(self, obj):
        return obj.owner.username

    def get_group(self, obj):
        return obj.group.title


class PostDetailSerializer(ModelSerializer):
    # HyperlinkedIdentityField
    delete_url = post_delete_url
    update_url = post_update_url

    # SerializerMethodFields
    owner = SerializerMethodField()

    class Meta:
        model = Blog
        fields = ('id', 'title', 'owner', 'update_url', 'delete_url')

    # get SerializerMethodField
    def get_owner(self, obj):
        return obj.owner.username

class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class PostDeleteSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class PostUpdateSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'




############ GROUP SERIALIZER ############

class GroupListSerializer(ModelSerializer):
    # my_posts = PostListSerializer(many=True, read_only=True)

    my_posts = SerializerMethodField()


    group = PostListSerializer(many=True, read_only=True)
    #### YOU CAN USE BELLOW LINKS TOO ###
    # group = StringRelatedField(many=True)
    # group = PrimaryKeyRelatedField(many=True, read_only=True)
    # group = HyperlinkedRelatedField(many=True, read_only=True, view_name='blog-api:post-detail', lookup_field='id')
    # group = SlugRelatedField(many=True, read_only=True, slug_field='title')


    class Meta:
        model = BlogGroup
        fields = ('id', 'title', 'my_posts', 'group')


    def get_my_posts(self, obj):
        # a = PostListSerializer(Blog.objects.all(), many=True, read_only=True, context={'request': self.context})
        # print obj.objects.all()
        # return PostListSerializer(many=True, read_only=True).data
        return 1

class GroupDetailSerializer(ModelSerializer):
    # posts = SerializerMethodField()

    class Meta:
        model = BlogGroup
        fields = ('title', 'posts')

    # def get_posts(self, obj):
    #     print obj.id
    #     print obj
    #     return Blog.objects.filter(group__id=1)



############ USER SERIALIZER ###########
from django.contrib.auth import get_user_model
User = get_user_model()

class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}