from django.conf.urls import patterns, include, url
from courses import views

urlpatterns = patterns('',	
	url(r'^(\d+)/$', views.course_detail, name='detail'),
	url(r'^add/$', views.create, name='add'),
	url(r'^edit/(?P<id>\d+)/$', views.edit, name='edit'),
	url(r'^remove/(?P<id>\d+)/$', views.remove, name='remove'),
	url(r'^(?P<id>\d+)/add_lesson$', views.add_lesson, name='add-lesson'),
)
