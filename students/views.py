# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from students.models import Student
from students.forms import StudentModelForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def list_view(request):
  course_id = request.GET.get('course_id', None)
  if course_id:
    students = Student.objects.filter(courses__id=course_id)
  else:
    students = Student.objects.all()
  return render(request, 'students/list.html', {'students': students})


def detail(request, pk):
  student = get_object_or_404(Student, pk=pk)
  return render(request, 'students/detail.html', {'student': student})


def create(request):
  if request.method == "POST":
    form = StudentModelForm(request.POST)
    if form.is_valid():
      student = form.save()
      messages.success(request, u'Student {} {} has been successfully added'.format(form.cleaned_data.get('name'), form.cleaned_data.get('surname')))
      return redirect('students:list_view')
  else:
    form = StudentModelForm()
  return render(request, 'students/add.html', {'form': form})

def edit(request, pk):
  student = get_object_or_404(Student, pk=pk)
  if request.method == "POST":
    form = StudentModelForm(request.POST, instance=student)
    if form.is_valid():
      student = form.save()
      messages.success(request, 'Info on the student has been sucessfully changed')
      return redirect('students:edit', student.id)
  else:
    form = StudentModelForm(instance=student)
  return render(request, 'students/edit.html', {'form': form})

def remove(request, pk):
  student = get_object_or_404(Student, pk=pk)
  if request.method == "POST":
    student.delete()
    messages.success(request, u'Info on {} {} has been sucessfully deleted'.format(student.name, student.surname))
    return redirect('students:list_view')
  return render(request, 'students/remove.html')