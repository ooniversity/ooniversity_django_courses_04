from django.conf.urls import patterns, include, url
from django.contrib import admin

from courses import views
import students

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pybursa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', views.index, name='index'),
    url(r'^(?P<course_id>\d+)/$', views.detail, name='detail'),

    url(r'^students/', include('students.urls', namespace='students')),
    
    url(r'^admin/', include(admin.site.urls)),
)