from django.conf.urls import patterns, include, url
from courses import views

urlpatterns = patterns('',
    url(r'^(\d+)/$', views.detail, name="detail"),
    url(r'^add/$', views.add, name="add"),
    url(r'^edit/(\d+)/$', views.edit, name="edit"),
    url(r'^remove/(\d+)/$', views.remove, name="remove"),
    url(r'^(\d+)/add_lesson$', views.add_lesson, name="add_lesson"),
)
