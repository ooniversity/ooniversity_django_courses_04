# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm

def detail(request, course_id):
    course_info = get_object_or_404(Course, id=int(course_id))
    lesson_list = Lesson.objects.filter(course_id=course_id)
    lesson_list.order_by('order')
    course_get = '?course_id=%d' % course_info.id
    s = {
         'lessons':lesson_list, 
         'course': course_info, 
         'course_get': course_get
        }
    return render(request, 'courses/detail.html', s)



def add(request):
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            application = form.save()
            messages.success(request, u'Course %s has been successfully added.' % (application.name))
            return redirect('index')
    else:
        form = CourseModelForm()
    return render(request, 'courses/add.html', {'form' : form})


def remove(request, course_id):
    course_inst = get_object_or_404(Course, id=course_id)    
    if request.method == 'POST':
        messages.success(request, u'Course %s has been deleted.' % (course_inst.name))
        course_inst.delete()
        return redirect('index')
    return render(request,'courses/remove.html', {'course': course_inst})


def edit(request, course_id):    
    course_inst = get_object_or_404(Course, id=course_id)    
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance = course_inst)
        if form.is_valid():
            form.save()
            messages.success(request, u'The changes have been saved.')
            return redirect('courses:edit', course_id)                
    else:
        form = CourseModelForm(instance = course_inst)
    return render(request, 'courses/edit.html', {'form': form})


def add_lesson(request, course_id):
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            messages.success(request, u'Lesson %s has been successfully added.' % (lesson.subject))
            return redirect('courses:detail', lesson.course.id)
    else:
        course=Course.objects.get(id=course_id)
        form = LessonModelForm(initial = {'course': course})
    return render(request, 'courses/add_lesson.html', {'form' : form})
