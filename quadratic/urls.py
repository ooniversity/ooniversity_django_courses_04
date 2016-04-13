# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from . import views

urlpatterns = patterns('',
    url(r'^results/$',views.quadratic_results,name='results'),
)



