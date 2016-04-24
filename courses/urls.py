from django.conf.urls import patterns, url
from courses import views

urlpatterns = patterns('',
    url(r'^(?P<course_id>\d+)/$', views.detail, name='detail'),
    url(r'^add/$', views.add, name = 'add'),
    url(r'^remove/(?P<id>\d+)/$', views.remove, name = 'remove'),
    url(r'^edit/(?P<id>\d+)/$', views.edit, name = 'edit'),
    url(r'^(?P<id>\d+)/add_lesson$', views.add_lesson, name='add-lesson'),
)