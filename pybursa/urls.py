from django.conf.urls import patterns, include, url
from django.contrib import admin
from pybursa import views
from students import views

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'views.index', name='index'),
    url(r'^contact/$', 'views.contact', name='contact'),
    url(r'^student_list/$', 'views.student_list', name='student_list'),
    url(r'^courses/1/', include('courses.urls', namespace="courses")),
    url(r'^students/?course_id=1', include('students.urls', namespace="students")),
    url(r'^students/1/$', views.detail, name='detail'),
)