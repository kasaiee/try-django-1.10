from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.PostListAPIView.as_view(), name='list'),
    # url(r'^(?P<id>[0-9]{1,3})$', views.detail, name='detail'),
]
