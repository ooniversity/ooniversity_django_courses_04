# -*- coding: cp1251 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

urlpatterns = patterns('',
    url(r'^$',views.index,name='index'),
    url(r'^feedback/', views.FeedbackView.as_view(),name='feedback'),
    url(r'^contact/$',views.contact,name='contact'),
    url(r'^student_detail/$',views.student_detail,name='student_detail'),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^quadratic/', include('quadratic.urls')),
    url(r'^courses/', include('courses.urls', namespace="courses")),
    url(r'^students/', include('students.urls', namespace="students")),
    url(r'^coaches/', include('coaches.urls', namespace="coaches")),
    url(r'^admin/', include(admin.site.urls)),
)
