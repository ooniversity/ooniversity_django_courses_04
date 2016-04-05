from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pybursa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
)
