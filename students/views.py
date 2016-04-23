# -*- coding: UTF-8 -*-
from django.shortcuts import render, redirect
from django.contrib import messages

from students.models import Student
from forms import StudentModelForm


def list_view(request):
    students_list = []

    if request.GET and request.GET['course_id']:
        course_id = request.GET['course_id']
        students_set = Student.objects.filter(courses=course_id)
    else:
        students_set = Student.objects.all()

    for student in students_set:
        student_detail = {
            'id':        student.id,
            'full_name': student.surname + ' ' + student.name,
            'address':   student.address,
            'skype':     student.skype,
            'courses':   student.courses.all(),
        }
        students_list.append(student_detail)

    return render(request, 'students/list.html', {'students_list': students_list})


def detail(request, student_id):
    student = Student.objects.get(id=student_id)
    student_courses = student.courses.all()
    parameters = {
        'student': student,
        'courses': student_courses,
    }
    return render(request, 'students/detail.html', parameters)


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
    return render(request, 'students/add.html', {'form': form})


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
