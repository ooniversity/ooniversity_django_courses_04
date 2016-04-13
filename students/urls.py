from django.conf.urls import patterns, include, url
from students import views
urlpatterns = patterns('',

    url(r'^$', views.list_view , name='lists'),
    url(r'^(?P<student_id>\d+)/$', views.detail, name='detail'),
)
