from django.conf.urls import patterns, url
from students import views

urlpatterns = patterns('',
    url(r'^(?P<id>\d+)/$', views.detail, name='detail'),
    url(r'^$', views.list_view, name='list_view'),
)