from django.conf.urls import patterns, include, url
from django.contrib import admin

from students import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pybursa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', views.index, name='index'),
    url(r'^$', views.list_view, name='list_view'),
    url(r'^(?P<student_id>\d+)/', views.detail, name='detail'),

    url(r'^admin/', include(admin.site.urls)),
)