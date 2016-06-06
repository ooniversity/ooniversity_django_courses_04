from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^(?P<course_id>\d+)/$', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    # # ex: /polls/5/vote/
)
