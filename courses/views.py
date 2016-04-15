from django.shortcuts import render
from courses.models import Course, Lesson


def detail(request, course_id):

    lesson = Lesson.objects.filter(course__id=course_id)
    course_details = Course.objects.get(id__exact=course_id)

    return render(request, 'courses/detail.html', {'details': course_details, 'lesson': lesson})