from django.conf.urls import patterns
from django.conf.urls import url

from courses import views


urlpatterns = patterns('',

    url(r'^(?P<pk>\d+)/$', views.CourseDetailView.as_view(), name='detail'),
    # url(r'^(?P<pk>\d+)/add_lesson$', views.add_lesson, name='add-lesson'),
    url(r'^(?P<pk>\d+)/add_lesson$', views.LessonCreateView.as_view(), name='add-lesson'),
    url(r'^add/$', views.CourseCreateView.as_view(), name='add'),
    url(r'^edit/(?P<pk>\d+)/$', views.CourseUpdateView.as_view(), name='edit'),
    url(r'^remove/(?P<pk>\d+)/$', views.CourseDeleteView.as_view(), name='remove'),

)
