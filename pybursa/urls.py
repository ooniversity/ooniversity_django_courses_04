from django.conf.urls import patterns, include, url

from django.contrib import admin

from pybursa  import views
#from pybursa.views import contact, student_list, student_detail, courses_info


urlpatterns = patterns('',
    url(r'^$', views.courses_info, name="index"),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^student_list/$', views.student_list, name='student_list'),
    url(r'^student_detail/$', views.student_detail, name='student_detail'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^quadratic/results/', include('quadratic.urls', namespace='quadratic')),
    url(r'^courses/', include('courses.urls', namespace="courses")),
    url(r'^students/', include('students.urls', namespace="students")),   
    url(r'^coaches/', include('coaches.urls', namespace="coaches")),
)
