<<<<<<< HEAD
from django.conf.urls import patterns, url

from quadratic import views

urlpatterns = patterns('',
	url(r'^results/$', views.quadratic_results, name='results'),
)
=======
from django.conf.urls import url, patterns

from . import views


urlpatterns = patterns('',
    url(r'^results/', views.quadratic_results, name='results'),
)

>>>>>>> f114d78577c0d563bac959a439787d0446e06ff9
