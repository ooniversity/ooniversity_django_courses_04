# encoding: utf-8
from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages

def create(request):
	if request.method == 'POST':
		form = CourseModelForm(request.POST)
		if form.is_valid():
			course = form.save()
			message = u" Course %s has been successfully added." %(course.name)
			messages.success(request, message)
			return redirect("index")
	else:
		form = CourseModelForm()

	return render(request, 'courses/add.html', {'form':form})


def edit(request, id):

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

    kurs = Course.objects.get(pk = id)
    if request.method == 'POST':
        kurs.delete()
        messages.success(request, u'Course %s has been deleted.'%kurs.name)
        return redirect('index')
    return render(request,"courses/remove.html", {"course": kurs})



def add_lesson(request,id):
	if request.method == 'POST':
		form = LessonModelForm(request.POST)
		if form.is_valid():
			lesson = form.save()
			message = u"Lesson %s has been successfully added." %(lesson.subject)
			messages.success(request, message)
			return redirect('courses:detail', lesson.course.id)
	else:


		course=Course.objects.get(pk=id)
		form = LessonModelForm(initial = {'course': course})
	return render(request, 'courses/add_lesson.html', {"form":form})


def detail(request, course_id):
    course = Course.objects.get(id=course_id)
    lesson = Lesson.objects.filter(course_id = course_id)
    return render(request, 'courses/detail.html',{'course':course, 'lesson':lesson})
