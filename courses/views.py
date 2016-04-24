from django.shortcuts import render, redirect
from django.contrib import messages
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm

def detail(request, courses__id):
    courses = Course.objects.filter(id = courses__id)
    lessons = Lesson.objects.filter(course_id = courses__id)
    return render(request, 'courses/detail.html', {'courses':courses, 'lessons':lessons})

def add(request):
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            courses = form.save()
            messages.success(request, 'Course %s has been successfully added.' %courses.name)
            return redirect('/')
    else:
        form = CourseModelForm()
    return render(request, 'courses/add.html', {'form':form})


def edit(request, courses__id):
    courses = Course.objects.get(id = courses__id)   
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=courses)
        if form.is_valid():
            courses = form.save()
            messages.success(request, 'The changes have been saved.')
            return redirect('courses:edit', courses__id)
    else:
        form = CourseModelForm(instance=courses)
    return render(request, 'courses/edit.html', {'form':form})

def remove(request, courses__id):
    courses = Course.objects.get(id = courses__id)
    if request.method == 'POST':
        courses.delete()
        messages.success(request, 'Course %s has been deleted.' %courses.name) 
        return redirect('/')         
    return render(request, 'courses/remove.html', {'courses':courses})

def add_lesson(request, courses__id):
    if request.method == 'POST':
        form = LessonModelForm(request.POST, initial={'course':courses__id})
        if form.is_valid():
            lessons = form.save()
            messages.success(request, "Lesson %s has been successfully added." % lessons.subject)
            return redirect('courses:detail', courses__id)
    else:
        form = LessonModelForm(initial={'course':courses__id})
    return render(request, 'courses/add_lesson.html', {'form':form})
