from django.conf.urls import patterns, include, url
from django.contrib import admin

from feedbacks import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pybursa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', views.index, name='index'),
    url(r'^$', views.FeedbackView.as_view(), name='feedback'),
    
)