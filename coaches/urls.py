from django.conf.urls import patterns, url
from coaches import views


urlpatterns = patterns('',
    url(r'^(\d+)/', views.coaches_detail_view, name='detail'),
    url(r'^', views.coaches_detail_view, name='courses'),
                       )