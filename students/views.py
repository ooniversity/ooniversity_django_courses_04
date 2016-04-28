# encoding: utf-8
from django.shortcuts import render, redirect
from students.models import Student
from courses.models import Course
from forms import StudentModelForm
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.template import RequestContext
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class StudentListView(ListView):
    """ Просмотр списка всех студентов"""
    model = Student
    paginate_by = 2
    
    #def get_paginator(self, queryset, page_size):
        #pag = super(StudentListView,self).get_paginator(queryset, page_size)
        #page = int(self.request.GET.get('page',1))
        #page = page if page < pag.num_pages else pag.num_pages
        #return pag.page(page)
       
    def get_context_data(self):
        context = super(StudentListView, self).get_context_data()
        context["course"] = Course.objects.all()
        #context["page_obj"] = self.get_paginator(self.get_queryset(), 2)        
        return context

    def get_queryset(self):
        course_id = self.request.GET.get('course_id', None)
        if not course_id:
            stud_list = Student.objects.all()
        else:
            stud_list = Student.objects.filter(courses__id = int(course_id))
        return stud_list


class StudentDetailView(DetailView):
    model = Student


class StudentCreateView(CreateView):
    """ Создание нового студента """
    model = Student
    success_url = reverse_lazy('students:list_view')
    form_class = StudentModelForm

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context["title"] = "Student registration"
        return context
    
    def form_valid(self,form):
        std = form.save()
        messages.success(self.request, u'Student %s %s has been successfully added.'%(std.name, std.surname))
        return super(StudentCreateView, self).form_valid(form)


class StudentUpdateView(UpdateView):
    """ Редактирование данных существующего студента """
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context["title"] = "Student info update"
        return context
    
    def form_valid(self,form):
        std = form.save()
        messages.success(self.request, u'Info on the student has been sucessfully changed.')
        return super(StudentUpdateView, self).form_valid(form)
    

class StudentDeleteView(DeleteView):
    """ Удаление студента с подтверждением """
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context["title"] = "Student info suppression"
        return context

