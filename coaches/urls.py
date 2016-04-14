
from django.conf.urls import patterns, include, url
from coaches import views

urlpatterns = patterns('',
    #url(r'^$', views.detail,name='detail'),
    url(r'^(?P<num>\d*)/$', views.detail, name='detail'),


)
   
