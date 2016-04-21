# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from django.contrib import messages
from courses.forms import CourseModelForm, LessonModelForm


def detail(request, course_id):
    lesson = Lesson.objects.filter(course_id=course_id)
    course = Course.objects.get(id=course_id)
    return render(request, 'courses/detail.html', {'course': course, 'lesson': lesson})


def add(request):
    if request.method == "POST":
        form = CourseModelForm(request.POST)
        if form.is_valid():
            new_course = form.save()
            new_message = u'Course %s has been successfully added.' % new_course.name
            messages.success(request, new_message)
            return redirect("/")
    else:
        form = CourseModelForm()
    return render(request, "courses/add.html", {'form': form})


def add_lesson(request, course_id):
    if request.method == "POST":
        form = LessonModelForm(request.POST)
        if form.is_valid():
            new_lesson = form.save()
            new_message = u'Lesson %s has been successfully added.' % new_lesson.subject
            messages.success(request, new_message)
            return redirect('courses:detail', new_lesson.course.id)
    else:
        form = LessonModelForm()
    return render(request, "courses/add_lesson.html", {'form': form})


def edit(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == "POST":
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            new_message = form.save()
            messages.success(request, u'The changes have been saved.')
            return redirect('courses:edit', new_message.id)
    else:
        form = CourseModelForm(instance=course)
    return render(request, "courses/edit.html", {'form': form})


def remove(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == "POST":
        course.delete()
        new_massage = u'Course %s has been deleted.' % course.name
        messages.success(request, new_massage)
        return redirect("/")
    return render(request, "courses/remove.html", {'name': course.name})
