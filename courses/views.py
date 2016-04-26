# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib import messages

from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm


def detail(request, course_id):
    course = Course.objects.get(id=course_id)
    lesson = Lesson.objects.filter(course_id = course_id)
    return render(request, 'courses/detail.html',{'course':course, 'lesson':lesson})

def add(request):
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid:
            app = form.save()
            messages.success(request, "Course %s has been successfully added." % app.name)
            return redirect('index')
    else:
        form = CourseModelForm()
    return render(request, 'courses/add.html', {'form': form})

def edit(request, course_id):
    app = Course.objects.get(id=course_id)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=app)
        if form.is_valid():
            app = form.save()
            messages.success(request, "The changes have been saved.")
        return redirect('courses:edit', course_id)
    else:
        form = CourseModelForm(instance=app)
    return render(request, 'courses/edit.html', {'form': form})

def remove(request, course_id):
    app = Course.objects.get(id=course_id)
    if request.method == 'POST':
        app.delete()
        messages.success(request, "Course %s has been deleted." % app.name)
        return redirect('index')
    return render(request, 'courses/remove.html', {'app': app})

def add_lesson(request, course_id):
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid:
            app = form.save()
            messages.success(request, "Lesson %s has been successfully added" % app.subject)
            return redirect('courses:detail', course_id)
    else:
        form = LessonModelForm(initial={'news_subscribe':True, 'course': course_id})
    return render(request, "courses/add_lesson.html", {'form': form})