from django.conf.urls import patterns, url

from coaches import views

urlpatterns = patterns('',
    url(r'^(?P<coach_id>\d+)/$', views.detail, name='detail'),
)