# -*- coding: UTF-8 -*-
from django.shortcuts import render, redirect
from django.contrib import messages
from courses.models import Course, Lesson
from forms import CourseModelForm, LessonModelForm

def detail(request, id_course):
    lesson = Lesson.objects.filter(course_id=id_course)
    course = Course.objects.get(id=id_course)
    return render(request, 'courses/detail.html', {'cur_course': course, 'cur_lesson': lesson})

def add(request):
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            data = form.save()
            message = u"Course %s has been successfully added." % (data.name)
            messages.success(request, message)
            return redirect('index')
    else:
        form = CourseModelForm()
    return render(request, 'courses/add.html', {'form': form})

def edit(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, u"The changes have been saved.")
            return redirect('courses:edit', course_id)
    else:
        form = CourseModelForm(instance=course)
    return render(request, "courses/edit.html", {'form': form})

def remove(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        course.delete()
        message = u"Course %s has been deleted." % (course.name)
        messages.success(request, message)
        return redirect('index')
    return render(request, "courses/remove.html", {'name': course.name})

def add_lesson(request, course_id):
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            message = u"Lesson %s has been successfully added." % (lesson.subject)
            messages.success(request, message)
            return redirect('courses:detail', course_id)
    else:
        form = LessonModelForm(initial={'course': course_id})
        return render(request, 'courses/add_lesson.html', {'form':form})
