from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField
from blog.models import Blog

class PostSerializer(ModelSerializer):

	class Meta:
		model = Blog
		# fields = ('title','content','owner')

		# get all fields
		fields = '__all__'
		
		# extra_kwargs = {'title': {'write_only': False}}