# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from courses import views


urlpatterns = patterns(
    '',
    url(r'^(?P<course_id>\d+)/$', views.detail, name='detail'),
    url(r'^add/$', views.add, name='add'),
    url(r'^(?P<course_id>\d+)/add_lesson$', views.add_lesson, name='add-lesson'),
    url(r'^edit/(?P<course_id>\d+)/$', views.edit, name='edit'),
    url(r'^remove/(?P<course_id>\d+)/$', views.remove, name='remove'),
)
