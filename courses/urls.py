from django.conf.urls import patterns, url
from courses import views

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', views.CourseDetailView.as_view(), name='detail'),
    url(r'^add/$', views.CourseCreateView.as_view(), name='add'),
    url(r'^edit/(?P<pk>\d+)/$', views.CourseUpdateView.as_view(), name='edit'),
    url(r'^remove/(?P<pk>\d+)/$', views.CourseDeleteView.as_view(), name='remove'),
    url(r'^(?P<pk>\d+)/add_lesson$', views.LessonCreateView.as_view(), name='add-lesson'),

    #url(r'^(?P<course_id>\d+)/$', views.detail, name='detail'),
    #url(r'^add/$', views.add, name = 'add'),
    #url(r'^remove/(?P<id>\d+)/$', views.remove, name = 'remove'),
    #url(r'^edit/(?P<id>\d+)/$', views.edit, name = 'edit'),
    #url(r'^(?P<id>\d+)/add_lesson$', views.add_lesson, name='add-lesson'),
)