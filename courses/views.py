from django.shortcuts import get_object_or_404
from django.shortcuts import render

from courses.models import Course
from courses.models import Lesson


def detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    lessons = Lesson.objects.filter(course=course).order_by('order')
    return render(request, 'courses/detail.html', {'course': course, 'lessons': lessons})
