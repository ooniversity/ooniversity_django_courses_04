from django.conf.urls import patterns, url

from students.views import stud_list_by_course_id, student_detail_by_id

urlpatterns = patterns('',
    url(r'^$', stud_list_by_course_id, name='list_by_course'),
    url(r'^(?P<student_id>\d+)/', student_detail_by_id, name='detail_by_id'),
)
