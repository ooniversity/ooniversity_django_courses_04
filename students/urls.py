# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from students import views

urlpatterns = patterns('',
    url(r'^$', views.StudentListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.StudentDetailView.as_view(), name='detail'),
    url(r'^add/$', views.StudentCreateView.as_view(), name='add'),
    url(r'^edit/(?P<pk>\d+)/$', views.edit, name='edit'),
    url(r'^remove/(?P<pk>\d+)/$', views.remove, name='remove'),
)
