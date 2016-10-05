from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.list, name='list'),
    url(r'^(?P<id>[0-9]{1,3})$', views.detail, name='detail'),
    url(r'^create/$', views.create, name='create'),
    url(r'^edit/(?P<id>[0-9]{1,3})$', views.edit, name='edit'),
    url(r'^delete/(?P<id>[0-9]{1,3})$', views.delete, name='delete'),
    url(r'^aa$', views.delete, name='search'),
]