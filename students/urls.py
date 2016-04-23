from django.conf.urls import patterns, url

from students import views


urlpatterns = patterns('',
                       url(r'^(\d+)/$',
                           views.student_detail_view, name="detail"),
                       url(r'^$', views.student_list_view, name="list_view"),
                       url(r'^add/$', views.create, name='add'),
                       url(r'^remove/(\d+)/$', views.remove, name='remove'),
                       url(r'^edit/(\d+)/$', views.edit, name='edit'),
                       )
