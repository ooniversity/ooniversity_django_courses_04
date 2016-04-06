from django.conf.urls import patterns, include, url
from django.contrib import admin
from pybursa import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^polls/', include('polls.urls',namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),

    #'http://127.0.0.1:8000/'                              =>  index                 => index                      => index.html
    url(r'^$', 'views.index', name='index'),

    #'http://127.0.0.1:8000/contact/'               => contact               => contact                  => contact.html
    url(r'^contact/', views.contact, name="contact"),
 
    #'http://127.0.0.1:8000/student_list/'        => student_list       => student_list           => student_list.html
    url(r'^student_list/', views.student_list, name="student_list"),
    

    #'http://127.0.0.1:8000/student_detail/'   => student_detail   => student_detail      => student_detail.html
    url(r'^student_detail/', views.student_detail, name="student_detail"),


)
   
