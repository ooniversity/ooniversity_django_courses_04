# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib import messages

from students.models import Student
from courses.models import Course
from students.forms import StudentModelForm

def create(request):	
	if request.method == 'POST':
		form = StudentModelForm(request.POST)
		if form.is_valid():
			application = form.save()
			message = u'Student %s %s has been successfully added.' % (application.name, application.surname)
			messages.success(request, message)
			return redirect('students:list_view')
	else:
		form = StudentModelForm()
	return render(request,'students/add.html', {'form': form})	


def edit(request, id):
	application = Student.objects.get(id=id)
	if request.method == 'POST':
		form = StudentModelForm(request.POST, instance=application)
		if form.is_valid():
			application = form.save()
			message = u'Info on the student has been successfully changed.'
			messages.success(request, message)
			#return redirect('students:edit')
	else:
		form = StudentModelForm(instance=application)
	return render(request,'students/edit.html', {'form': form})


def remove(request, id):
	application = Student.objects.get(id=id)
	if request.method == 'POST':
		application.delete()
		message = u'Info on %s %s has been sucessfully deleted.' % (application.name, application.surname)
		messages.success(request, message)
		return redirect('students:list_view')
	
	return render(request,'students/remove.html', {'ap':application})


def list_view(request):	
	if request.GET:
		course_id = request.GET['course_id']
		students = Student.objects.filter(courses=course_id).order_by('id')	
	else:
		students = Student.objects.all()
	
	return render(request, 'students/list.html', {'students':students})


def student_detail(request, id):
	student = Student.objects.get(id=id)
	return render(request, 'students/detail.html', {'student':student})
	
