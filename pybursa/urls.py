from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url
from django.contrib import admin

from pybursa import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pybursa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^quadratic/', include('quadratic.urls')),
    url(r'^courses/', include('courses.urls', namespace='courses')),
    url(r'^students/', include('students.urls', namespace='students')),
    url(r'^coaches/', include('coaches.urls', namespace='coaches')),
    url(r'^feedback/', include('feedbacks.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^student_list/', views.student_list, name='student_list'),
    url(r'^student_detail/', views.student_detail, name='student_detail'),

)
