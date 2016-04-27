from django.conf.urls import patterns, include, url
from django.contrib import admin

from students import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pybursa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', views.index, name='index'),
    url(r'^$', views.StudentListView.as_view(), name='list_view'),
    url(r'^(?P<pk>\d+)/', views.StudentDetailView.as_view(), name='detail'),
    url(r'^add/', views.StudentCreateView.as_view(), name='add'),
    url(r'^edit/(?P<pk>\d+)/', views.StudentUpdateView.as_view(), name='edit'),
    url(r'^remove/(?P<pk>\d+)/', views.StudentDeleteView.as_view(), name='remove'),

    url(r'^admin/', include(admin.site.urls)),
)