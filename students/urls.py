from django.conf.urls import patterns, url
from students import views

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', views.StudentDetailView.as_view(), name='detail'),
    url(r'^edit/(?P<pk>\d+)/$', views.StudentUpdateView.as_view(), name='edit'),
    url(r'^remove/(?P<pk>\d+)/$', views.StudentDeleteView.as_view(), name='remove'),
    url(r'^add/$', views.StudentCreateView.as_view(), name='add'),
    url(r'^$', views.StudentListView.as_view(), name='list_view'),
)