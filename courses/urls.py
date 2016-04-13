# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from courses import views


urlpatterns = patterns(
    '',
    url(r'^(\d+)/$', views.course_detail_view, name="detail"),
)
