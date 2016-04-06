from django.conf.urls import patterns, include, url
from django.contrib import admin
from pybursa.views import main_page, contact, studlist,	studdetail

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pybursa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
   	url(r'^$', main_page, name='main_page'),

	url(r'^contact/', contact, name='contact'),

	url(r'^student_list/', studlist, name='student_list'),

	url(r'^student_detail/', studdetail, name='student_detail'),
   
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),

)