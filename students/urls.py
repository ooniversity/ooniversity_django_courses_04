from django.conf.urls import patterns, include, url
from students import views
urlpatterns = patterns('',

    url(r'^$', views.list_view, name='list_view'),
    url(r'^(?P<student_id>\d+)/$', views.detail, name='detail'),
    url(r'^add/$', views.add_student, name='add'),
    url(r'^edit/(?P<pk>\d+)/$', views.edit_student, name='edit'),
)
