from django.conf.urls import patterns, include, url
from students import views

urlpatterns = patterns('',
	url(r'^(?P<id>\d+)/$', views.student_detail, name='detail'),
	url(r'^$', views.list_view, name='list_view'),
)
