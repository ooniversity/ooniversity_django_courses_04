from django.conf.urls import patterns, include, url, handler404, handler500
from django.contrib import admin
from pybursa import views
from feedbacks.views import FeedbackView
handler404 = 'pybursa.views.my_custom_page_not_found_view'
handler500 = 'pybursa.views.my_custom_error_view'


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^quadratic/', include('quadratic.urls', namespace="quadratic")),
    url(r'^courses/', include('courses.urls', namespace="courses")),
    url(r'^students/', include('students.urls', namespace="students")),
    url(r'^coaches/', include('coaches.urls', namespace="coaches")),
    url(r'^feedback/$', FeedbackView.as_view(), name="feedback"),

    url(r'^admin/', include(admin.site.urls)),
)
