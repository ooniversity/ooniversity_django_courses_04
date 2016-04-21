from django.conf.urls import patterns, url
from courses import views


urlpatterns = patterns('',
    url(r'^(?P<course_id>\d+)/$', views.detail, name='detail'),
    url(r'^add/$', views.add, name='add'),
    url(r'^edit/(?P<pk>\d+)/$', views.edit, name='edit'),
)
