from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^(?P<teacher_id>\d+)/$', views.detail, name='detail'),
)
