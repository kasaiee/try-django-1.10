from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField
from blog.models import Blog

class PostListSerializer(ModelSerializer):
	class Meta:
		model = Blog
		fields = ('title', 'owner',)		
		# extra_kwargs = {'title': {'write_only': False}}


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


