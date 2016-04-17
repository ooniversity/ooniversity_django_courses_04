from django.conf.urls import patterns, include, url
from django.contrib import admin
#from django.http import HttpResponse
#import current functions_views
from pybursa.views import contact, student_list, student_detail, courses_info


urlpatterns = patterns('',
    url(r'^$', courses_info, name="index"),
    url(r'^contact/$', contact, name='contact'),
    url(r'^student_list/$', student_list, name='student_list'),
    url(r'^student_detail/$', student_detail, name='student_detail'),
#polls and admins added during tutorial 1-4
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls', namespace="polls")),
# quadratic test
    url(r'^quadratic/results/', include('quadratic.urls')),
#DJ adm stuff
    url(r'^courses/', include('courses.urls', namespace="courses")),
    url(r'^students/', include('students.urls', namespace="students")),   
    url(r'^coaches/', include('coaches.urls', namespace="coaches")),
)
