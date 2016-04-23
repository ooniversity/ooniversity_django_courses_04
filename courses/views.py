# encoding: utf-8
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from courses.models import Course, Lesson
from coaches.models import Coach
from courses.forms import CourseModelForm, LessonModelForm



def detail(request,course_id):
    course = get_object_or_404(Course, pk=course_id)
    lessons = Lesson.objects.filter(course=course).order_by('order')
    return render(request, 'courses/detail.html',
           {"course":course,
            "lessons":lessons,
            })

def add(request):
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            application = form.save()
            msg = u"Course %s has been successfully added." % (application.name)
            messages.success(request, msg)
            return redirect('index')
    else:
        form = CourseModelForm()
    return render(request, 'courses/add.html', {'form': form})


def edit(request, course_id):
    application = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=application)
        if form.is_valid():
            application = form.save()
            messages.success(request, u"The changes have been saved.")
            return redirect('courses:edit', application.id)
    else:
        form = CourseModelForm(instance=application)
    return render(request, 'courses/edit.html', {'form': form})


def remove(request, course_id):
    application = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        application.delete()
        msg = u"Course %s has been deleted." % (application.name)
        messages.success(request, msg)
        return redirect('index')
    notice = u"The cource %s will be removed" % (application.name)
    return render(request, 'courses/remove.html', {'notice': notice})


def add_lesson(request, course_id):
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            application = form.save()
            msg = u"Lesson %s has been successfully added." % (application.subject)
            messages.success(request, msg)
            return redirect('courses:detail', application.course.id)
    else:
        form = LessonModelForm(initial = {'course': course_id})
    return render(request, 'courses/add_lesson.html', {'form': form})
