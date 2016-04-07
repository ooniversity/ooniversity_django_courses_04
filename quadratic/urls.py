from django.conf.urls import patterns, url
from quadratic import views

urlpatterns = patterns('',
 
    # ex:  /quadratic/results/?
    url(r'^$', views.quadratic_results, name='results'),

)
