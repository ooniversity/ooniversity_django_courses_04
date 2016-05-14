# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render, redirect
from datetime import date
from students.models import Student
from courses.models import Course
from forms import StudentModelForm
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

import logging
logger = logging.getLogger(__name__)

class StudentListView(ListView):
    model = Student
    #template_name = 'students/list.html'
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
        context['course_id'] = self.request.GET.get('course_id', None)
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
    if request.GET:
        course_id = int(request.GET['course_id'])
        course = get_object_or_404(Course, id=course_id)
        list_of_students = course.student_set.all()
        list_of_students.order_by('id')
    else:
        list_of_students = Student.objects.all()
        list_of_students.order_by('id')

    student_courses = dict()
    for stud in list_of_students:
        student_courses[stud.id] = stud.courses.all()
    return render(request, 'students/list.html', {'students_list': list_of_students, 'course_list': student_courses})

def detail(request, student_id):
    student = get_object_or_404(Student, id=int(student_id))
    student_courses_list = student.courses.all()
    return render(request, 'students/detail.html', {'student':student, 'students_courses':student_courses_list})

def create(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            std = form.save()
            messages.success(request, u'Student %s %s has been successfully added.'%(std.name, std.surname))
            return redirect('students:list_view')
                
    else:
        form = StudentModelForm()
    return render(request,"students/add.html",{"form":form})

def edit(request, id):  
    std_instance = Student.objects.get(pk = id)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance = std_instance)
        if form.is_valid():
            std = form.save()
            messages.success(request, u'Info on the student has been sucessfully changed.')
            return redirect('students:list_view')
                
    else:
        form = StudentModelForm(instance = std_instance)
    return render(request,"students/edit.html",{"form": form})

def remove(request, id):
    std = Student.objects.get(pk = id)
    if request.method == 'POST':
        messages.success(request, u'Info on %s %s has been sucessfully deleted.'%(std.name, std.surname))
        std.delete()
        return redirect('students:list_view')
    return render(request,"students/remove.html", {"student": std})