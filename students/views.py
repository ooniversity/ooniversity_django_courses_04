# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from students.models import Student
from django.contrib import messages
from students.forms import StudentModelForm


def student_list_view(request):
    if request.GET.get('course_id') is None:
        student = Student.objects.all()
        return render(request, 'students/list.html', {'students': student})
    else:
        student = Student.objects.filter(courses__id=request.GET.get('course_id'))
        return render(request, 'students/list.html', {'students': student})


def student_detail_view(request, student_id):
        student = Student.objects.get(id=student_id)
        return render(request, 'students/detail.html', {'students': student})


def student_create_view(request):
    if request.method == "POST":
        form = StudentModelForm(request.POST)
        if form.is_valid():
            student = form.save()
            new_message = "Student %s %s has been successfully added." % (student.name, student.surname)
            messages.success(request, new_message)
            return redirect("students:list_view")
    else:
        form = StudentModelForm()
    return render(request, "students/add.html", {'form': form})


def student_update_view(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == "POST":
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            new_message = "Info on the student has been sucessfully changed."
            messages.success(request, new_message)
    else:
        form = StudentModelForm(instance=student)
    return render(request, "students/edit.html", {'form': form})


def student_delete_view(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == "POST":
        student.delete()
        new_message = "Info on %s %s has been sucessfully deleted." % (student.name, student.surname)
        messages.success(request, new_message)
        return redirect("students:list_view")
    return render(request, "students/remove.html", {'name': student.name, 'surname': student.surname})
