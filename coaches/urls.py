from django.conf.urls import patterns, url

from coaches import views

urlpatterns = patterns('',
url(r'^$', views.detail, name='detail'),
)