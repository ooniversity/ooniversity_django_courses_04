# encoding: utf-8
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from courses.models import Course, Lesson
from coaches.models import Coach


def detail(request,course_id):
    course = get_object_or_404(Course, pk=course_id)
    lessons = Lesson.objects.filter(course=course).order_by('order')
    #course_coaches = Coach.objects.filter(course=course)#.order_by('order')
    return render(request, 'courses/detail.html',
           {"course":course,
            "lessons":lessons,
            #"coaches":course_coaches,
            })

