from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import index, contact, student_list, student_detail

urlpatterns = patterns('',
    # Examples:
    url(r'^$', index),
    url(r'^contact$', contact),
    url(r'^student_list$', student_list),
    url(r'^student_detail$', student_detail),
    # url(r'^blog/', include('blog.urls')),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
)
