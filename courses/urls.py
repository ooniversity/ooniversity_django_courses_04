from django.conf.urls import patterns, url
from courses import views

urlpatterns = patterns('',
    url(r'^(?P<courses__id>\d+)/$', views.detail, name='detail'),
)
