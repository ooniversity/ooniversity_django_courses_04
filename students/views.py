# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from students.models import Student
from django.utils.datastructures import MultiValueDictKeyError
from forms import StudentModelForm
from django.contrib import messages


def list_view(request):
    try:
        a = request.GET['course_id']
        stud_at_course = Student.objects.filter(courses__id=a)
    except MultiValueDictKeyError:
        stud_at_course = Student.objects.all()
    return render(request, 'students/list.html', {'stud': stud_at_course})


def detail(request, student_id):
    stud_table = Student.objects.get(id=student_id)
    return render(request, 'students/detail.html', {'student': stud_table})


def add_student(request):
    if request.method == 'POST':
        add_form = StudentModelForm(request.POST)
        if add_form.is_valid():
            a = add_form.cleaned_data['name']
            b = add_form.cleaned_data['surname']
            add_form.save()
            msg = 'Студент {0} {1} был добавлен.'.format(a, b)
            messages.success(request, msg)
            return redirect('students:list_view')
    else:
        add_form = StudentModelForm()
    return render(request, 'students/add.html', {'add_s': add_form})
