
from django.conf.urls import patterns, include, url
from students import views


urlpatterns = patterns('',
    url(r'^(?P<num>\d+)', views.student_detail, name='student_detail'),
    url(r'^$', views.student_list,name='student_list'),


)
   
