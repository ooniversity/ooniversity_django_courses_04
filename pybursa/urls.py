from django.conf.urls import patterns, include, url, handler404, handler500
from django.contrib import admin

from pybursa import views
import polls
import courses
import coaches
import feedbacks

handler404 = 'pybursa.views.server_error_404'
handler500 = 'pybursa.views.server_error_500'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pybursa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^courses/', include('courses.urls', namespace='courses')),
    url(r'^students/', include('students.urls', namespace='students')),
    url(r'^coaches/', include('coaches.urls', namespace='coaches')),

    url(r'^polls/', include('polls.urls', namespace='polls')),

    url(r'^contact/$', views.contact, name='contact'),
    url(r'^student_list/$', views.student_list, name='student_list'),
    url(r'^student_detail/$', views.student_detail, name='student_detail'),

    url(r'^feedback/$', include('feedbacks.urls')),
    
    url(r'^quadratic/results/', include('quadratic.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
)