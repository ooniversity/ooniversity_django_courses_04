# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from students.models import Student
from forms import StudentModelForm
from django.contrib import messages


def list_view(request):
	if request.GET:
		deskr = Student.objects.filter(courses__id=int(request.GET['course_id']))
	else:
		deskr = Student.objects.all()
	return render(request, 'students/list.html', {'deskr':deskr})


def detail(request, student_id):
	det = Student.objects.get(id=student_id)
	return render(request, 'students/detail.html', {'det':det})

def create(request):
	if request.method == 'POST':
		form = StudentModelForm(request.POST)
		if form.is_valid():
			create_st = form.save()
			messages.success(request, "Student %s %s has been successfully added." % (create_st.name, create_st.surname))
			return redirect('students:list_view')
	else:
		form = StudentModelForm()
	return render(request, 'students/add.html', {'form':form})

def edit(request, student_id):
	edit_st = Student.objects.get(id=student_id)
	if request.method == 'POST':
		form = StudentModelForm(request.POST, instance=edit_st)
		if form.is_valid():
			form.save()
			messages.success(request, 'Данные изменены')
			return redirect('students:edit', student_id)
	else:
		form = StudentModelForm(instance=edit_st)
	return render(request, 'students/edit.html', {'form':form})


def remove(request, student_id):
	remov = Student.objects.get(id=student_id)
	if request.method == 'POST':
		remov.delete()
		messages.success(request, "Info on %s %s has been successfully deleted." % (remov.name, remov.surname))
		return redirect('students:list_view')
	return render(request, 'students/remove.html', {'remov':remov})
