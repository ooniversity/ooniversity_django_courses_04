from django.conf.urls import patterns, include, url, handler404, handler500
from django.contrib import admin
from pybursa.views import index, student_list, contact, student_detail
from feedbacks.views import FeedbackView


handler404 = 'pybursa.views.custom404'
handler500 = 'pybursa.views.custom500'


urlpatterns = patterns('',
                       url(r'^$', index, name='index'),
                       url(r'^contact/$', contact, name='contact'),
                       url(r'^student_list/$',
                           student_list, name='student_list'),
                       url(r'^student_detail/$',
                           student_detail, name='student_detail'),
                       url(r'^polls/',
                           include('polls.urls', namespace="polls")),
                       url(r'^quadratic/',
                           include('quadratic.urls', namespace="quadratic")),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^courses/',
                           include('courses.urls', namespace="courses")),
                       url(r'^students/',
                           include('students.urls', namespace="students")),
                       url(r'^coaches/',
                           include('coaches.urls', namespace="coaches")),
                       url(r'^feedback/$',
                           FeedbackView.as_view(), name='feedback'),
                       )
