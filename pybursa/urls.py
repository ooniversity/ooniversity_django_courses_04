from django.conf.urls import patterns, include, url
from django.contrib import admin
from pybursa.views import index, student_list, contact, student_detail

urlpatterns = patterns('',
                       url(r'^$', index, name='index'),
                       url(r'^contact/$', contact, name='contact'),
                       url(r'^student_list/$',
                           student_list, name='student_list'),
                       url(r'^student_detail/$',
                           student_detail, name='student_detail'),
                       url(r'^polls/',
                           include('polls.urls', namespace="polls")),
                       url(r'^admin/', include(admin.site.urls)),
                       )
