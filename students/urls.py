from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.list_view, name='list_view'),
    url(r'^add/$', views.create, name='add'),
    url(r'^(?P<student_id>\d+)/$', views.detail, name='detail'),
)
