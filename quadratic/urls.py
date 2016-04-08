# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from . import views

urlpatterns = patterns('',
    # url(r'^$',views.quadratic_results,name='results2'),
    url(r'^results/$',views.quadratic_results,name='equation'),#(?P<b>\d+)
    # url(r'^equation/', , name = 'equation')

    # url(r'^results/(?P<b>\d+)$',views.quadratic_results,name='results'),#(?P<b>\d+)
)#results/



