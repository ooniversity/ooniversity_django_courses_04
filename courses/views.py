from django.shortcuts import render
from courses.models import Course, Lesson


# Create your views here.

def course_detail_view(request, id_course):
    course = Course.objects.get(id=id_course)
    lesson = Lesson.objects.filter(course_id=id_course)
    return render(request, 'courses/detail.html',
                  {"course": course, "lesson": lesson})
