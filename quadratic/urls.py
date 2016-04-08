from django.conf.urls import url, patterns

from . import views


urlpatterns = patterns('',
    url(r'^$', views.quadratic_results, name='results'),
)

