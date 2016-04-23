from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from django.contrib import messages
from courses.forms import CourseModelForm, LessonModelForm

def course_detail(request, id_course):
	lesson = Lesson.objects.filter(course_id=id_course)
	course = Course.objects.get(id=id_course)
	return render(request, 'courses/detail.html', {'course': course, 'lesson':lesson})


def create(request):	
	if request.method == 'POST':
		form = CourseModelForm(request.POST)
		if form.is_valid():
			application = form.save()
			message = u'Course %s has been successfully added.' % (application.name)
			messages.success(request, message)
			return redirect('/')
	else:
		form = CourseModelForm()

	return render(request,'courses/add.html', {'form':form})	


def edit(request, id):
	application = Course.objects.get(id=id)
	if request.method == 'POST':
		form = CourseModelForm(request.POST, instance=application)
		if form.is_valid():
			application = form.save()
			message = u'The changes have been saved.'
			messages.success(request, message)
			return redirect('courses:edit', application.id)			
	else:
		form = CourseModelForm(instance=application)

	return render(request,'courses/edit.html', {'form':form})


def remove(request, id):
	application = Course.objects.get(id=id)
	if request.method == 'POST':
		application.delete()
		message = u'Course %s has been deleted.' % (application.name)
		messages.success(request, message)
		return redirect('/')
	
	return render(request,'courses/remove.html', {'ap':application})


def add_lesson(request, id):	
	if request.method == 'POST':
		form = LessonModelForm(request.POST)
		if form.is_valid():
			application = form.save()
			message = u'Lesson %s has been successfully added.' % (application.subject)
			messages.success(request, message)
			return redirect('courses:detail', application.course.id)
	else:
		course = Course.objects.get(id=id)		
		form = LessonModelForm(initial={'course':course})

	return render(request,'courses/add_lesson.html', {'form':form})

