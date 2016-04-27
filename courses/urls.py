from django.conf.urls import patterns, url
from courses import views

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<id>\d+)/add_lesson$', views.add_lesson, name='add-lesson'),
    url(r'^add/$', views.add, name='add'),
    url(r'^edit/(?P<pk>\d+)/$', views.edit, name='edit'),
    url(r'^remove/(?P<pk>\d+)/$', views.remove, name='remove'),
)