# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from courses import views

urlpatterns = patterns(
    '',
    url(r'^(?P<pk>\d+)/$', views.CourseDetailView.as_view(), name='detail'),

)
