# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from courses.models import Course
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def detail(request, pk):
  course = get_object_or_404(Course, pk=pk)
  return render(request, 'courses/detail.html', {'course': course})

def create(request):
  if request.method == "POST":
    form = CourseModelForm(request.POST)
    if form.is_valid():
      course = form.save()
      messages.success(request, u'Course {} has been successfully added.'.format(course.name))
      return redirect('index')
  else:
    form = CourseModelForm()
  return render(request, 'courses/add.html', {'form': form})

def edit(request, pk):
  course = get_object_or_404(Course, pk=pk)
  if request.method == "POST":
    form = CourseModelForm(request.POST, instance=course)
    if form.is_valid():
      course = form.save()
      messages.success(request, 'The changes have been saved.')
      return redirect('courses:edit', course.id)
  else:
    form = CourseModelForm(instance=course)
  return render(request, 'courses/edit.html', {'form': form})

def remove(request, pk):
  course = get_object_or_404(Course, pk=pk)
  if request.method == "POST":
    course.delete()
    messages.success(request, u'Course {} has been deleted.'.format(course.name))
    return redirect('index')
  return render(request, 'courses/remove.html', {'course': course})

def add_lesson(request, pk):
  course = get_object_or_404(Course, pk=pk)
  if request.method == "POST":
    form = LessonModelForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'Lesson lesson_name has been successfully added.'.format(lesson.subject))
      return redirect('courses:detail', lesson.course.id)
  else:
    form = LessonModelForm(request.POST)
  return render(request, 'courses/add_lesson.html', {'form': form})
