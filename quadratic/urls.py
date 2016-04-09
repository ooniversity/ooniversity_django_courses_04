from django.conf.urls import patterns, url

from quadratic import views

urlpatterns = patterns('',
    url(r'^$', views.results, name='results'),
    
)
