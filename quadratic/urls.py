from django.conf.urls import patterns, include, url
from django.contrib import admin

from quadratic import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pybursa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.quadratic_results, name='results'),
)