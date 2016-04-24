from django.conf.urls import patterns, url
from courses import views

urlpatterns = patterns('',
    url(r'^(?P<courses__id>\d+)/$', views.detail, name='detail'),
    url(r'^add/$', views.add, name='add'),
    url(r'^edit/(?P<courses__id>\d+)/$', views.edit, name='edit'),
    url(r'^remove/(?P<courses__id>\d+)/$', views.remove, name='remove'), 
    url(r'^(?P<courses__id>\d+)/add_lesson/$', views.add_lesson, name='add-lesson'),
)
