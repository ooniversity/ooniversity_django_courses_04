from django.shortcuts import render
from courses.models import Course, Lesson


def detail(request, id_course):
    course_detail = Lesson.objects.filter(course_id=id_course).values()
    course = Course.objects.filter(id=id_course).values()
    return render(request, 'courses/detail.html', locals())
