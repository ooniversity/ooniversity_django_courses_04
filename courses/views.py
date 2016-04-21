# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render, redirect
from courses.models import Course,Lesson
from forms import CourseModelForm, LessonModelForm
from django.contrib import messages

def create(request):
	if request.method == 'POST':
		form = CourseModelForm(request.POST)
		if form.is_valid():
			course = form.save()
			message = u" Course %s has been successfully added." %(course.name)
			messages.success(request, message)
			return redirect("/")
	else:
		form = CourseModelForm()

	return render(request, 'courses/add.html', {'form':form})

def edit(request,id):
	course_inst = Course.objects.get(pk=id)
	if request.method == 'POST':
		form = CourseModelForm(request.POST, instance=course_inst)
		if form.is_valid():
			course= form.save()
			message = u"The the changes has been saved."
			messages.success(request, message)
			return redirect('courses:detail',course_inst.id)
	else:
		form = CourseModelForm(instance=course_inst)
	
	return render(request,"courses/edit.html",{"form":form})
  

def remove(request,id):
    course = Course.objects.get(pk=id)
    if request.method == 'POST':
        course.delete()
        message = u"Course %s  has been deleted." %(course.name)
        messages.success(request, message)
        return redirect("/")
    return render(request,"courses/remove.html",{"name":course.name})

def add_lesson(request):
	if request.method == 'POST':
		form = LessonModelForm(request.POST)
		if form.is_valid():
			lesson = form.save()
			message = u"Lesson %s has been successfully added." %(lesson.subject)
			messages.success(request, message)
			return redirect('courses:detail', lesson.course.id)
	else:
		form = LessonModelForm()

	return render(request, 'courses/add_lesson.html', {"form":form})



def detail(request, course_id):
    course = Course.objects.get(id=course_id)
    lesson = Lesson.objects.filter(course_id = course_id)
    return render(request, 'courses/detail.html',{'course':course, 'lesson':lesson})




