from django.conf.urls import patterns, url
from courses import views

urlpatterns = patterns('',
    url(r'^(?P<id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<id>\d+)/add-lesson/$', views.add_lesson, name='add-lesson'),
    url(r'^add/$', views.add, name='add'),
    url(r'^edit/(?P<id>\d+)/$', views.edit, name='edit'),
    url(r'^remove/(?P<id>\d+)/$', views.remove, name='remove'),
)