# -*- coding: UTF-8 -*-
from django.shortcuts import render, redirect
from django.contrib import messages
from students.models import Student
from forms import StudentModelForm

def list_view(request):
    if request.GET.get('course_id') == None:
        student = Student.objects.all()
        return render(request, 'students/list.html', {'cur_students': student})
    else:
        student = Student.objects.filter(courses__id=request.GET.get('course_id'))
        return render(request, 'students/list.html', {'cur_students': student})

def detail(request, student_id):
        student = Student.objects.get(id=student_id)
        return render(request, 'students/detail.html', {'cur_students': student})

def create(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            data = form.save()
            message = u"Student %s %s has been successfully added." % (data.name, data.surname) 
            messages.success(request, message)
            return redirect('students:list_view')
    else:
        form = StudentModelForm()
    return render(request, 'students/add.html', {'add_form': form})

def edit(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, u"Info on the student has been sucessfully changed.")
    else:
        form = StudentModelForm(instance=student)
    return render(request, "students/edit.html", {'form': form})


def remove(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        student.delete()
        message = u"Info on %s %s has been sucessfully deleted." % (student.name, student.surname)
        messages.success(request, message)
        return redirect("students:list_view")
    return render(request, "students/remove.html", {'name': student.name, 'surname': student.surname})
