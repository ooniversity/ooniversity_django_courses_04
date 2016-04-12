from django.conf.urls import patterns, include, url
from students import views

urlpatterns = patterns('',
    url(r'^$', views.stud, name="stud"),
    url(r'^(\d+)/$', views.list_view, name="list_view"),
)
