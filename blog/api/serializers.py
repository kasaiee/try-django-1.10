from blog.models import Blog
from rest_framework.serializers import (
    ModelSerializer, 
    HyperlinkedIdentityField,
    )


post_detail_url = HyperlinkedIdentityField(
    view_name='blog-api:detail',
    lookup_field='id'
    )


post_delete_url = HyperlinkedIdentityField(
    view_name='blog-api:delete',
    lookup_field='id'
    )


post_update_url = HyperlinkedIdentityField(
    view_name='blog-api:update',
    lookup_field='id'
    )


class PostListSerializer(ModelSerializer):
    detail_url = post_detail_url
    delete_url = post_delete_url
    update_url = post_update_url
    
    class Meta:
        model = Blog
        fields = ('id', 'title', 'owner', 'detail_url', 'update_url', 'delete_url')
        # extra_kwargs = {'title': {'write_only': False}}


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


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