from django.shortcuts import render
from courses.models import Course, Lesson


def detail(request, courses__id):
    courses = Course.objects.filter(id = courses__id)
    lessons = Lesson.objects.filter(course_id = courses__id)
    return render(request, 'courses/detail.html', {'courses':courses, 'lessons':lessons})

