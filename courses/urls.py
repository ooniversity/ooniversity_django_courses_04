from django.conf.urls import patterns, include, url
from courses import views


urlpatterns = patterns('',
    url(r'^(?P<id>\d+)/add_lesson/$', views.add_lesson, name='add-lesson'),#include(patterns('courses.views',url(r'^add_lesson$', views.add_lesson, name = 'add-lesson'),)),
    url(r'^(?P<pk>\d+)/$', views.CourseDetailView.as_view(), name = 'detail'),
    url(r'^(?P<id>\d+)/add_lesson$', views.add_lesson, name='add-lesson'),
    #url(r'^(?P<num>\d*)/$', views.detail, name = 'detail'),
    url(r'^add/$', views. CourseCreateView.as_view(), name = 'add'),
    url(r'^remove/(?P<pk>\d+)/$', views.CourseDeleteView.as_view(), name = 'remove'),
    url(r'^edit/(?P<pk>\d+)/$', views.CourseUpdateView.as_view(), name = 'edit'),
    )
   
