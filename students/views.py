# -*- coding: utf-8 -*-
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

from courses.models import Course
from students.forms import StudentModelForm
from students.models import Student

import logging
logger = logging.getLogger(__name__)


class StudentListView(ListView):
    model = Student
    paginate_by = 2

    def get_queryset(self):
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            qs = Student.objects.filter(courses__id=course_id)
        else:
            qs = Student.objects.all()
        return qs

    def get_context_data(self, **kwargs):
        context = super(StudentListView, self).get_context_data(**kwargs)
        course_id = self.request.GET.get('course_id', None)
        context['course_prefix'] = 'course_id={0}&'.format(course_id) if course_id else ''
        return context


class StudentDetailView(DetailView):
    model = Student

    def get_context_data(self, **kwargs):
        logger.debug("Students detail view has been debugged")
        logger.info("Logger of students detail view informs you!")
        logger.warning("Logger of students detail view warns you!")
        logger.error("Students detail view went wrong!")
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        return context


class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Student registration'
        context['btn_name'] = u'Создать'
        return context

    def form_valid(self, form):
        messages.set_level(self.request, messages.SUCCESS)
        messages.success(self.request, u'Student {0} {1} has been successfully added.'.format(form.cleaned_data.get('name'), form.cleaned_data.get('surname')))
        return super(StudentCreateView, self).form_valid(form)


class StudentUpdateView(UpdateView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Student info update'
        context['btn_name'] = u'Изменить'
        return context

    def form_valid(self, form):
        messages.set_level(self.request, messages.SUCCESS)
        messages.success(self.request, 'Info on the student has been sucessfully changed.')
        return super(StudentUpdateView, self).form_valid(form)


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        messages.set_level(self.request, messages.WARNING)
        messages.warning(self.request, u'Are you sure you want to delete "{0} {1}"?'.format(kwargs['object'].name, kwargs['object'].surname))
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Student info suppression'
        return context

    def delete(self, request, *args, **kwargs):
        student = Student.objects.get(pk=kwargs['pk'])
        messages.set_level(self.request, messages.SUCCESS)
        messages.success(request, u'Info on {0} {1} has been sucessfully deleted.'.format(student.name, student.surname))
        return super(StudentDeleteView, self).delete(request, *args, **kwargs)


def list_view(request):
    course = None
    try:
        course = get_object_or_404(Course, pk=request.GET['course_id'])
        students = Student.objects.filter(courses=course)
    except MultiValueDictKeyError:
        students = Student.objects.all()
    context = []
    for student in students:
        context.append({'student': student})
    return render(request, 'students/list.html',
            {'context': context, 'course':course})


def detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'students/detail.html', {'student': student})


def create(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.set_level(request, messages.SUCCESS)
            messages.success(request, u'Student {0} {1} has been successfully added.'.format(form.cleaned_data.get('name'), form.cleaned_data.get('surname')))
            return redirect('students:list_view')
    else:
        form = StudentModelForm()
    return render(request, 'students/add.html', {'form': form})


def edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.set_level(request, messages.SUCCESS)
            messages.success(request, 'Info on the student has been sucessfully changed.')
            redirect('students:edit', pk=pk)
    else:
        form = StudentModelForm(instance=student)
    return render(request, 'students/edit.html', {'form': form})


def remove(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        messages.set_level(request, messages.SUCCESS)
        messages.success(request, u'Info on {0} {1} has been sucessfully deleted.'.format(student.name, student.surname))
        return redirect('students:list_view')
    else:
        messages.set_level(request, messages.WARNING)
        messages.warning(request, u'Are you sure you want to delete {0} {1}'.format(student.name, student.surname))
    return render(request, 'students/remove.html')
