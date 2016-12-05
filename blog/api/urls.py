from django.conf.urls import url
import views

urlpatterns = [
    url(r'^user$', views.UserListAPIView.as_view(), name='user-list'),
    url(r'^user/create$', views.UserCreateAPIView.as_view(), name='user-create'),


    # POST GROUP API
    url(r'^groups$', views.GroupListAPIView.as_view(), name='group-list'),
    url(r'^groups/(?P<id>\d+)$', views.GroupDetailAPIView.as_view(), name='group-detail'),

    # #id in bellow url, must defined in PostDetailAPIView as lookup_field field
    # url(r'^(?P<id>\d+)$', views.PostDetailAPIView.as_view(), name='detail'),
    
    # url(r'^(?P<id>\d+)/delete$', views.PostDeleteAPIView.as_view(), name='delete'),
    # url(r'^(?P<id>\d+)/update$', views.PostUpdateAPIView.as_view(), name='update'),

    # url(r'^create/$', views.PostCreateAPIView.as_view(), name='create'),



    # POST API
    url(r'^posts$', views.PostListAPIView.as_view(), name='post-list'),

    #id in bellow url, must defined in PostDetailAPIView as lookup_field field
    url(r'^posts/(?P<id>\d+)$', views.PostDetailAPIView.as_view(), name='post-detail'),
    
    url(r'^posts/(?P<id>\d+)/delete$', views.PostDeleteAPIView.as_view(), name='post-delete'),
    url(r'^posts/(?P<id>\d+)/update$', views.PostUpdateAPIView.as_view(), name='post-update'),

    url(r'^posts/create/$', views.PostCreateAPIView.as_view(), name='post-create'),

]
