from django.conf.urls import patterns
from django.conf.urls import url

from courses import views


urlpatterns = patterns('',

    url(r'^(?P<course_id>\d+)/$', views.detail, name='detail'),

)
