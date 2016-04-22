from django.conf.urls import patterns
from django.conf.urls import url

from courses import views


urlpatterns = patterns('',

    url(r'^(?P<course_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<course_id>\d+)/add_lesson$', views.add_lesson, name='add-lesson'),
    url(r'^add/$', views.add, name='add'),
    url(r'^edit/(?P<pk>\d+)/$', views.edit, name='edit'),
    url(r'^remove/(?P<pk>\d+)/$', views.remove, name='remove'),

)
