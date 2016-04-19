
from django.conf.urls import patterns, include, url
from students import views


urlpatterns = patterns('',
    url(r'^$', views.list_view,name='list_view'),
    url(r'^(?P<num>\d*)/$', views.detail, name='detail'),
    url(r'^add/$', views.create, name='add'),
    url(r'^remove/$', views.remove, name='remove'),
    url(r'^edit/$', views.edit, name='edit'),


)
   
