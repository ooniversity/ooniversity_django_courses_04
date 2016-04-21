from django.conf.urls import patterns, url
from students import views

urlpatterns = patterns('',
    url(r'^(?P<id>\d+)/$', views.detail, name='detail'),
    url(r'^edit/(?P<id>\d+)/$', views.edit, name='edit'),
    url(r'^remove/(?P<id>\d+)/$', views.remove, name='remove'),
    url(r'^add/$', views.create, name='add'),
    url(r'^$', views.list_view, name='list_view'),
)