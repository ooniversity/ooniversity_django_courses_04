# -*- coding: utf-8 -*-

from django.shortcuts import render
from .models import Course, Lesson


def detail(request, course_id):
    course = Course.objects.get(pk=course_id)
    lessons = Lesson.objects.filter(course=course_id)
    context = {'course': course, 'lessons': lessons}
    return render(request, 'courses/detail.html', context)
