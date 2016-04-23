from django.conf.urls import patterns, url

from students import views

urlpatterns = patterns('',
    url(r'^$', views.stud_list_by_course_id, name='list_view'),
    url(r'^(?P<student_id>\d+)/', views.student_detail_by_id, name='detail'),
    url(r'^add/$', views.create, name='add'),
    url(r'^edit/(?P<student_id>\d+)/$', views.edit, name='edit'),
    url(r'^remove/(?P<student_id>\d+)/$', views.remove, name='remove'),
)
