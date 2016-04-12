# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from students import views

urlpatterns = patterns(
    '',
    url(r'^$', views.StudentListView.as_view(), name='list_view'),
    url(r'^(?P<pk>\d+)/$', views.StudentDetailView.as_view(), name='detail'),

)
