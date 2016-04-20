from django.conf.urls import patterns, url
from students import views

urlpatterns = patterns('',
	url(r'^$', views.list_view, name='list_view'),
	url(r'^(?P<student_id>\d+)/', views.detail, name='detail'),
	url(r'^add/$', views.create,  name='student-adding'),
	url(r'^add/$', views.edit,  name='student-edit'),
	url(r'^add/$', views.remove,  name='student-remove'),
)

