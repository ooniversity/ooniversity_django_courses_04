from django.conf.urls import patterns, url
from students import views
from students.views import StudentDetailView
  
urlpatterns = patterns('',
	#url(r'^$', views.list_view, name='list_view'),
	url(r'^$', views.StudentListView.as_view(), name='list_view'),
	# url(r'^(?P<student_id>\d+)/$', views.detail, name="detail"),	
	url(r'^(?P<pk>\d+)/$', views.StudentDetailView.as_view(), name='detail'),
    url(r'^add/', views.StudentCreateView.as_view(), name='add'),
    url(r'^edit/(?P<pk>\d+)/$', views.StudentUpdateView.as_view(), name='edit'), 
    #url(r'^edit/(?P<id>\d*)/', views.edit, name='edit'),
    url(r'^remove/(?P<pk>\d+)/$', views.StudentDeleteView.as_view(), name='remove')
    #url(r'^remove/(?P<id>\d*)/', views.remove, name='remove')
)
