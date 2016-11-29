from rest_framework import generics
from .serializers import PostSerializer
from blog.models import Blog

class PostListAPIView(generics.ListAPIView):
	'''
	**this is a **
	simple documentation for api
	'''

	queryset = Blog.objects.all()
	serializer_class = PostSerializer