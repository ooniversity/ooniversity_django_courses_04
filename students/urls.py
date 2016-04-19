# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from students import views


urlpatterns = patterns(
    '',
    url(r'^$', views.student_list_view, name="list_view"),
    url(r'^(\d+)/$', views.student_detail_view, name="detail"),
    url(r'^add/$', views.student_create_view, name="add"),
    url(r'^edit/(?P<student_id>\d+)/$', views.student_update_view, name="edit"),
    url(r'remove/(?P<student_id>\d+)/$', views.student_delete_view, name="remove"),
)
