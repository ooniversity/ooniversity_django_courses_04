from django.conf.urls import patterns, include, url
from courses import views


urlpatterns = patterns('',
    url(r'^(?P<id>\d+)/add_lesson/$', views.add_lesson, name='add-lesson'),#include(patterns('courses.views',url(r'^add_lesson$', views.add_lesson, name = 'add-lesson'),)),
    url(r'^(?P<pk>\d*)/$', views.detail, name = 'detail'),
    url(r'^(?P<id>\d+)/add_lesson$', views.add_lesson, name='add-lesson'),
    url(r'^(?P<num>\d*)/$', views.detail, name = 'detail'),
    url(r'^add/$', views.add, name = 'add'),
    url(r'^remove/(?P<id>\d+)/$', views.remove, name = 'remove'),
    url(r'^edit/(?P<id>\d+)/$', views.edit, name = 'edit'),
    )
   
