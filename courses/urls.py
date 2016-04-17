from django.conf.urls import url, patterns
from django.http import HttpResponse
from courses import views


urlpatterns = patterns('',
    url(r'(\d+)/$', views.detail, name='detail'),
    url(r'^', views.detail, name='courses'),
                       )
