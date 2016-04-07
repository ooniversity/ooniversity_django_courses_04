from django.conf.urls import patterns, include, url
from django.contrib import admin
from quadratic.views import calc_equation

urlpatterns = patterns('',
    # Examples:
    url(r'^results/', calc_equation),
)
