# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from students.models import Student
from courses.models import Course
from forms import StudentModelForm
from django.contrib import messages
from django.template import RequestContext
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class StudentListView(ListView):
	model = Student
	paginate_by = 2

	def	get_queryset(self):
		qs =  super(StudentListView, self).get_queryset()
		course_id =self.request.GET.get('course_id', None)
		if course_id:
			qs = qs.filter(courses__id=course_id)
		return qs	

class StudentDetailView(DetailView):
	model = Student
	


class StudentCreateView(CreateView):
	model = Student
	success_url = reverse_lazy('students:list_view')
	form_class = StudentModelForm
		
	def get_context_data(self,**kwargs):
		context = super(StudentCreateView, self).get_context_data(**kwargs)
		context['title'] = u"Student registration"
		return context

	def form_valid(self,form):
		student = form.save()
		messages.success(self.request, u'Student %s %s has been successfully added.'%(student.name, student.surname))
		return super(StudentCreateView, self).form_valid(form)	

class StudentUpdateView(UpdateView):
	model = Student
	success_url = reverse_lazy('students:list_view')

	def get_context_data(self,**kwargs):
		context = super(StudentUpdateView, self).get_context_data(**kwargs)
		context['title'] = u"Student info update"
		return context
	
	def form_valid(self,form):
		student = form.save()
		messages.success(self.request, u'Student %s %s has been successfully added.'%(student.name, student.surname))
		return super(StudentUpdateView, self).form_valid(form)

class StudentDeleteView(DeleteView):
	model = Student

	success_url = reverse_lazy('students:list_view')
	
	def get_context_data(self,**kwargs):
		context = super(StudentDeleteView, self).get_context_data(**kwargs)
		context['title'] = u"Student info suppression"
		return context
