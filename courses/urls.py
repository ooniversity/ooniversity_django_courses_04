from django.conf.urls import patterns, include, url
from courses import views


urlpatterns = patterns('',
   url(r'^(?P<num>\d*)/$', views.detail,name='detail'),
   #url(r'^', views.detail, name='list'),

)
   
