from django.conf.urls import patterns
from django.conf.urls import url

from coaches import views


urlpatterns = patterns('',

    url(r'^(?P<coach_id>\d+)/$', views.detail, name='detail'),

)
