from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.PostListAPIView.as_view(), name='list'),

    #id in bellow url, must defined in PostDetailAPIView as lookup_field field
    url(r'^(?P<id>\d+)$', views.PostDetailAPIView.as_view(), name='detail'),
    
    url(r'^create/$', views.PostCreateAPIView.as_view(), name='create'),
]
