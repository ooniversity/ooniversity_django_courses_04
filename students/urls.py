
from django.conf.urls import patterns, include, url
from students import views


urlpatterns = patterns('',
    url(r'^$', views.student_list,name='list'),
    url(r'^(?P<num>\d+)/$', views.student_detail, name='detail'),


)
   
