from django.conf.urls import patterns, url

from students import views


urlpatterns = patterns('',
                       url(r'^(\d+)/$', views.student_detail_view, name="detail"),
                       url(r'^$', views.student_list_view, name="list"),
                       )
