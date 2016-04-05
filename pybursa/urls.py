from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import index, contact, student_list, student_detail


urlpatterns = patterns(
    '',
    # Examples:
    url(r'^$', index, name='main'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^student_list/$', student_list, name='student_list'),
    url(r'^student_detail/$', student_detail, name='student_detail'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

)
