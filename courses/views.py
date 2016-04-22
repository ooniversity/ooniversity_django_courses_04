# -*- coding: utf-8 -*-
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from courses.forms import CourseModelForm
from courses.forms import LessonModelForm
from courses.models import Course
from courses.models import Lesson


def detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    lessons = Lesson.objects.filter(course=course).order_by('order')
    return render(request, 'courses/detail.html', {'course': course, 'lessons': lessons})

def add(request):
    form = CourseModelForm()
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.set_level(request, messages.SUCCESS)
            messages.success(request, u'Course {0} has been successfully added.'.format(form.cleaned_data.get('name')))
            return redirect('index')
    return render(request, 'courses/add.html', {'form': form})


def edit(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.set_level(request, messages.SUCCESS)
            messages.success(request, 'The changes have been saved.')
            redirect('courses:edit', pk=pk)
    else:
        form = CourseModelForm(request.POST, instance=course)
    return render(request, 'courses/edit.html', {'form': form})


def remove(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        messages.set_level(request, messages.SUCCESS)
        messages.success(request, u'Course {0} has been deleted.'.format(course.name))
        return redirect('index')
    else:
        messages.set_level(request, messages.WARNING)
        messages.warning(request, u'Are you sure you want to delete {0}'.format(course.name))
    return render(request, 'courses/remove.html')


def add_lesson(request, course_id):
    lesson = Lesson()
    lesson.course = get_object_or_404(Course, pk=course_id)
    lesson.order = Lesson.objects.filter(course=lesson.course).count() + 1
    form = LessonModelForm(instance=lesson)
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.set_level(request, messages.SUCCESS)
            messages.success(request, u'Lesson {0} has been successfully added.'.format(form.cleaned_data.get('subject')))
            return redirect('courses:detail', course_id=course_id)
    return render(request, 'courses/add_lesson.html', {'form': form})
