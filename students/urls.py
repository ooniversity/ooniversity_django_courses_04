# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from students import views

urlpatterns = patterns(
    '',
    url(r'^$', views.student_list_view, name="list_view"),
    url(r'^(\d+)/$', views.student_detail_view, name="detail"),
)
