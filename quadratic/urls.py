from django.conf.urls import url, patterns
from django.http import HttpResponse
from quadratic import views


urlpatterns = patterns('',
    url(r'results/$', views.quadratic_results, name='results'),)
