from django.conf.urls import url, patterns

from quadratic import views

urlpatterns=patterns('',
    url(r'^results/',views.quadratic_results, name='results'),
    #url(r"^results/",views.index, name='index'),

)
