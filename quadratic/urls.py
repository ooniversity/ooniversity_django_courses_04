from django.conf.urls import patterns
from django.conf.urls import url

from quadratic import views


urlpatterns = patterns('',
    url(r'^results/', views.quadratic_results, name='results'),
)
