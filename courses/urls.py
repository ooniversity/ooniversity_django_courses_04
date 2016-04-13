# encoding: utf-8
from django.conf.urls import patterns, url
from courses import views

urlpatterns = patterns('',
    # url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<course_id>\d+)/$', views.detail, name='detail'),
    # url(r'^(?P<course_id>\d+)/$', views.detail, name='detail'),

)
