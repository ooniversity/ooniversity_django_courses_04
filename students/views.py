# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages

from students.models import Student
from courses.models import Course
from students.forms import StudentModelForm

def list_view(request):
	course_id = request.GET.get('course_id')

	if course_id:
		students = Student.objects.filter(courses__id=course_id)
	else:
		students = Student.objects.all()	
	return render(request, 'students/list_view.html', locals())

def detail(request, student_id):
	student = Student.objects.get(id=student_id)
	student_courses = student.courses.all()
	return render(request, 'students/detail.html', locals())

def create(request):
    if request.method == "POST":
    	form = StudentModelForm(request.POST)
    	if form.is_valid():
    		application = form.save()
    		message = u"Student %s %s has been successfully added." % (application.name, application.surname)
    		messages.success(request, message)
    		return redirect('students:list_view')
    else:
        form = StudentModelForm()	
    return render(request, 'students/add.html', {'form':form}) 

def remove(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == "POST":
        message =  u"Info on %s %s has been sucessfully deleted." % (student.name, student.surname)
        student.delete()
        messages.success(request, message)
        return redirect('students:list_view')
    else:
        return render(request, 'students/remove.html', {'student':student})

def edit(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    students = Student.objects.all()
    if request.method == "POST":
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Студент  был изменен.")
            return render(request, 'students/list_view.html', locals())
    else:
        form = StudentModelForm(instance=student)
    return render(request, 'students/edit.html', {'form':form})