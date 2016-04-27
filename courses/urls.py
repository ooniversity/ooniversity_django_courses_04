from django.conf.urls import patterns, include, url
from courses import views

urlpatterns = patterns('',
	url(r'^(?P<pk>\d+)/$', views.CourseDetailView.as_view(), name='detail'),
	url(r'^add/$', views.CourseCreateView.as_view(), name='add'),
	url(r'^edit/(?P<pk>\d+)/$', views.CourseUpdateView.as_view(), name='edit'),
	url(r'^remove/(?P<course_id>\d+)/$', views.remove, name='remove'),
	url(r'^(?P<course_id>\d+)/add_lesson$', views.add_lesson, name='add-lesson'),
)