from django.conf.urls import patterns, include, url
from django.contrib import admin
from pybursa import views

admin.site.site_header = 'PyBursa Administration'
#admin.site.index_template='admin/index.html'

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^polls/', include('polls.urls',namespace="polls")),

    url(r'^quadratic/', include('quadratic.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^index/', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^contact/', views.contact, name="contact"),
 
    #url(r'^student_list/', views.student_list, name="student_list"),
    
    #url(r'^student_detail/', views.student_detail, name="student_detail"),

    url(r'^courses/', include('courses.urls',namespace="courses")),
    #url(r'^courses/$', name='courses_list'),
 
    url(r'^students/', include('students.urls',namespace="students")),
    url(r'^coaches/', include('coaches.urls',namespace="coaches")),


)
   
