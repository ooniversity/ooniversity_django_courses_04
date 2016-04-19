# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from students import views


urlpatterns = patterns(
    '',
    url(r'^$', views.student_list_view, name="list_view"),
    url(r'^(\d+)/$', views.student_detail_view, name="detail"),
    url(r'^add/$', views.create, name="add"),
    url(r'^edit/(?P<student_id>\d+)/$', views.edit, name="edit"),
    url(r'^remove/(?P<student_id>\d+)/$', views.remove, name="remove"),
)
