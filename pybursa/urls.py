from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render

from pybursa import views

#moved to views.py
#def index(request):
#    print 'Start index view'
#    return render(request, 'index.html')

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),    
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^student_list/$', views.student_list, name='student_list'),
    url(r'^student_detail/$', views.student_detail, name='student_detail'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^quadratic/results/', include('quadratic.urls')),
    
)
