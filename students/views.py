#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from students.models import Student
from students.forms import StudentModelForm


class StudentListView(ListView):
    model = Student
        
    def get_queryset(self):
        qs = super(StudentListView, self).get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id: 
            qs = qs.filter(courses__id=course_id) 
        return qs


class StudentDetailView(DetailView):
    model = Student


class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title']='Student registration'
        return context

    def form_valid(self, form):
        self.application = form.save()
        messages.success(self.request, u'Student {} {} has been successfully added.'.format(self.application.name, self.application.surname))
        return super(StudentCreateView, self).form_valid(form)            
          

class StudentUpdateView(UpdateView):
    model = Student

    def get_success_url(self, **kwargs):
        return reverse_lazy('students:edit', args = [self.object.pk,])

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Student info update'
        return context
        
    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Info on the student has been successfully changed.')
        return super(StudentUpdateView, self).form_valid(form)     


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Student info suppression'
        return context

    def delete(self, request, *args, **kwargs):
        student = super(StudentDeleteView, self).delete(request, *args, **kwargs)
        messages.success(self.request, u'Info on {} {} has been successfully deleted.'.format(self.object.name, self.object.surname)) 
        return student


