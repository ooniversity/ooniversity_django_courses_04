from django.conf.urls import patterns, include, url
from django.contrib import admin

from quadratic import quadratic_results

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pybursa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^results/', quadratic_results.quadratic_results, name='results'),
    url(r'^admin/$', include(admin.site.urls)),
)