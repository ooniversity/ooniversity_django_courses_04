# -*- coding: cp1251 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

urlpatterns = patterns('',
    url(r'^(\d+)$', views.detail, name='detail'),
    url(r'^', views.list_view, name='students'),

)