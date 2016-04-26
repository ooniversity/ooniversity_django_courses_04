# encoding: utf-8
from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages


def detail(request, pk):
    """ Информация о курсах """
    course = Course.objects.get(pk = pk)
    lessons_list = Lesson.objects.filter(course_id = pk)
    return render(request, "courses/detail.html", {"course": course, "lessons_list": lessons_list})

def add(request):
    """ Создание нового курса """
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            curs = form.save()
            messages.success(request, u'Course %s has been successfully added.'%(curs.name))
            return redirect('index')
    else:
        form = CourseModelForm()
    return render(request,"courses/add.html",{"form":form})

def edit(request, id):
    """ Редактирование данных существующего курса """
    kurs = Course.objects.get(pk = id)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance = kurs)
        if form.is_valid():
            kurs = form.save()
            messages.success(request, u'The changes have been saved.')
            return redirect('courses:edit', kurs.id)
                
    else:
        form = CourseModelForm(instance = kurs)
    return render(request,"courses/edit.html",{"form": form})

def remove(request, id):
    """ Удаление курса с подтверждением """
    kurs = Course.objects.get(pk = id)
    if request.method == 'POST':
        kurs.delete()
        messages.success(request, u'Course %s has been deleted.'%kurs.name)
        return redirect('index')
    return render(request,"courses/remove.html", {"course": kurs})

def add_lesson(request,id):
    """ Добавление нового урока для конкретного курса """
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            messages.success(request, u'Lesson %s has been successfully added.'%(lesson.subject))
            return redirect('courses:detail', lesson.course.id)
    else:
        course=Course.objects.get(pk=id)
        form = LessonModelForm(initial = {'course': course})
    return render(request,"courses/add_lesson.html",{"form":form})

