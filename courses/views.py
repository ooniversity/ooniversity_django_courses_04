# -*- coding: utf-8 -*-

from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Course, Lesson
from .forms import CourseModelForm, LessonModelForm


def detail(request, course_id):
    course = Course.objects.get(pk=course_id)
    lessons = Lesson.objects.filter(course=course_id)
    context = {'course': course, 'lessons': lessons}
    return render(request, 'courses/detail.html', context)


def add(request):
    if request.method == "POST":
        form = CourseModelForm(request.POST)
        if form.is_valid():
            course = form.save()
            messages.success(
                request, "Course %s has been successfully added!" % 
                course.name)
        return redirect('index')
    else:
        form = CourseModelForm()
    return render(request, 'courses/add.html', {'form': form})
 

def edit(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == "POST":
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save()
            messages.success(request, "The changes have been saved!")
        return redirect('courses:edit', course.id)
    else:
        form = CourseModelForm(instance=course)
    return render(request, 'courses/edit.html', {'form': form})   


def remove(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        course.delete()
        messages.success(
            request, "Course %s has been deleted!" % course.name)
        return redirect('index')
    else:
        return render(request, 'courses/remove.html', {'course': course})