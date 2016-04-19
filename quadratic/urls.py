from django.conf.urls import patterns, include, url
from quadratic.views import quadratic_results

urlpatterns = patterns('',
    # Examples:
    url(r'^results/', quadratic_results, name='equation'),
)
